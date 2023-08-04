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

        # Locate files we need within that directory

        tokenizer_path = os.path.join(model_directory, "tokenizer.model")
        model_config_path = os.path.join(model_directory, "config.json")
        st_pattern = os.path.join(model_directory, "*.safetensors")
        model_path = glob.glob(st_pattern)[0]

        # Create config, model, tokenizer and generator

        config = ExLlamaConfig(model_config_path)  # create config from config.json
        config.model_path = model_path  # supply path to model weights file

        model = ExLlama(config)  # create ExLlama instance and load the weights
        tokenizer = ExLlamaTokenizer(tokenizer_path)  # create tokenizer from tokenizer model file

        cache = ExLlamaCache(model)  # create cache for inference
        self.generator = ExLlamaGenerator(model, tokenizer, cache)  # create generator

        # Configure generator

        self.generator.disallow_tokens([tokenizer.eos_token_id])

        self.generator.settings.token_repetition_penalty_max = 1.2
        self.generator.settings.temperature = 0.95
        self.generator.settings.top_p = 0.65
        self.generator.settings.top_k = 100
        self.generator.settings.typical = 0.5
        
    def predict(self, prompt):

        output = self.generator.generate_simple(prompt, max_new_tokens=200)
        return output[len(prompt):]
    
    # def generate_to_eos(self, prompt):
    #
    #     self.generator.end_beam_search()
    #
    #     ids = self.tokenizer.encode(prompt)
    #     num_res_tokens = ids.shape[-1]  # Decode from here
    #     self.generator.gen_begin(ids)
    #
    #     new_text = ""
    #
    #     self.generator.begin_beam_search()
    #     for i in range(max_new_tokens):
    #         gen_token = self.generator.beam_search()
    #         if gen_token.item() == self.tokenizer.eos_token_id:
    #             print("EOS found")
    #             return new_text
    #
    #         num_res_tokens += 1
    #         text = self.tokenizer.decode(self.generator.sequence_actual[:, -num_res_tokens:][0])
    #         new_text = text[len(prompt):]
    #         print(i)
    #         print(new_text)
    #         if new_text.lower().endswith(stop_sequence.lower()):
    #             print("Stop sequence found")
    #             return new_text[:-len(stop_sequence)]
    #
    #     return new_text
