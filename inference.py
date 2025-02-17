import glob
import os

from exllama.generator import ExLlamaGenerator
from exllama.model import ExLlama, ExLlamaCache, ExLlamaConfig
from exllama.tokenizer import ExLlamaTokenizer

from config import model_name, max_new_tokens, token_repetition_penalty_max, temperature, top_p, top_k


stop_sequence = "###"


class Predictor:
    def setup(self):
        # Model moved to network storage
        model_directory = f"/runpod-volume/{model_name}"

        # snapshot_download(repo_id=repo_name, local_dir=model_directory)
        tokenizer_path = os.path.join(model_directory, "tokenizer.model")
        model_config_path = os.path.join(model_directory, "config.json")
        st_pattern = os.path.join(model_directory, "*.safetensors")
        model_path = glob.glob(st_pattern)[0]

        config = ExLlamaConfig(model_config_path)               # create config from config.json
        config.model_path = model_path                          # supply path to model weights file
        config.max_input_len = 16384                            # set max input length to 16K tokens
        config.max_output_len = 16384                           # set max output length to 16K tokens
        config.max_seq_len = 16384                              # set max sequence length to 16K tokens

        """Load the model into memory to make running multiple predictions efficient"""
        print("Loading tokenizer...")

        self.tokenizer = ExLlamaTokenizer(tokenizer_path)            # create tokenizer from tokenizer model file

        print("Loading model...")

        self.model = ExLlama(config)                                 # create ExLlama instance and load the weights

        print("Creating cache...")
        self.cache = ExLlamaCache(self.model)                             # create cache for inference

        print("Creating generator...")
        self.generator = ExLlamaGenerator(self.model, self.tokenizer, self.cache)   # create generator

        # Configure generator
        self.generator.disallow_tokens([self.tokenizer.eos_token_id])

        self.generator.settings.token_repetition_penalty_max = token_repetition_penalty_max
        self.generator.settings.temperature = temperature
        self.generator.settings.top_p = top_p
        self.generator.settings.top_k = top_k
        self.generator.settings.max_new_tokens = 2048
        
    def predict(self, prompt):

        return self.generate_to_eos(prompt)
    
    def generate_to_eos(self, prompt):

        self.generator.end_beam_search()

        ids = self.tokenizer.encode(prompt)
        num_res_tokens = ids.shape[-1]  # Decode from here
        self.generator.gen_begin(ids)

        new_text = ""

        self.generator.begin_beam_search()
        for i in range(max_new_tokens):
            gen_token = self.generator.beam_search()
            if gen_token.item() == self.tokenizer.eos_token_id:
                print("EOS found")
                return new_text

            num_res_tokens += 1
            text = self.tokenizer.decode(self.generator.sequence_actual[:, -num_res_tokens:][0])
            new_text = text[len(prompt):]
            if new_text.lower().endswith(stop_sequence.lower()):
                print("Stop sequence found")
                return new_text[:-len(stop_sequence)]

        return new_text
