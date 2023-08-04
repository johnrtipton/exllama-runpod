import os

import requests
import time

# The URL of the rupod serverless endpoint
endpoint_id = "l934nklbjdmiy0"
url = f"https://api.runpod.ai/v2/{endpoint_id}"

# The json data to send to the /run endpoint
data = {
    "input": {
        "prompt": """You are an expert meeting note taker, your job is to get business value and insight from meeting transcriptions.
USER: Transcript: OK, so as I said, this is useful as a way of proving that two sets are equal, and we're
going to see that in the next result. So this is going to be another proposition. This is going to be the distributive laws.
For set unions and intersections. So this time we're going to let, A and B and C be
some subsets of a set s, and then the claim is that A
union B intersect C is the same as a union B intersect A Union C. It's kind of telling
me that I can expand the brackets. That's what distributive means.
And the second law is that A intersect B union C (this is just the other way round) is the
same as A intersect B union A intersect C.
You can think of these actually in terms of a Venn diagram as well. If this is A,
B and C, then that first set is A union B intersect C, which is this region here.
And, the distributive law is kind of telling us that we can think of that set in two different ways,
either as the union of A and B intersect C, or as the intersection of A union B and A
union C, and you can think about that in terms of the diagram.
So let's prove this. I'm only going to prove the first one. I'll leave the second one for
you. So we're going to try and show that the left hand side here is a subset of the right hand
side, and then we're going to show that the right hand side is a subset of the left hand side, and that will show that they're the same set.
OK, so first of all, I'm going to suppose that I have an X which is in the left hand
side and then try and show that it's in the right hand side. So it X is in the left hand side, it means X is in A or X is in B and X is in C.
So I'm going to say, then X is in A or X is in B and X is in C. I'm using brackets just
to clarify how that sentence works.
OK, and now in either of these cases, if X is in A, then certainly it's in A union B
and it's also in A union C. So if we're in this case, then we are certainly in the intersection of those two sets.
If we're in this case that X is in B and C, then for different reasons, X is in A union B and it's in A union C, because of being in B and C. So again, it will be
in the intersection, so it will be in the right hand side.
So I want to write out something to explain that. So I'm going to say in either case,
X is going to be in A union B and X is going to be in A union C, so X is in the right hand
side. i.e., the left hand side is a subset of the right hand side.
OK, now we're going to go the other way round, so we're going to say conversely,
suppose X is in the right hand side.
So X is in this set here.
So then I'll write, then X is in A union B and X is in A union C.
And so in order for X to be in A union B there are two ways that could happen. X could be in A, or X could be in B. If X is in A, then it's automatically in here,
so that's one option. If X is not in A, then it must be in B in order for this to hold.
And in order for this to hold, it must be in C. So there are two cases.
X is in A, or,
I say, if X is not in A, then X is in B and X is in C. So in that second case, X is in
the intersection of B and C. So I'll say, and therefore X is in the intersection of B and C. And it could be in all of these
things, but either it's in A or if it's not in A, then it must be in the intersection of B and C, and that exactly means that it must be
in the union of A and B intersect C,
So I'll say, hence X is in A
union B intersect C, which is the left hand side. So we've shown that the right hand side
is a subset of the left hand side. So the left [should be right] hand side is a subset of the right [should be left] hand
side. Right. Then we bring those together, so I'll say hence by double inclusion,
the left hand side and the right hand side are equal.
OK, so it was a similar kind of argument where it's helpful to split it up into two separate
bits. I want to show one more proposition, and this is quite an important one,
about how complements of unions and intersections work. This is called De Morgan's Laws.
So this time we're just going to need two subsets, so let A and B be subsets of S.
Then we have two things.
First of all, the complement of the union, A union B, is the intersection of the complement
of A and the complement of B. And secondly, the other way round, the complement of the intersection is the union of the complements.
So this is kind of telling you that you could take the complement through the brackets, provided that you change the union into an intersection and the intersection into a union.
So this is quite an important rule. So let's try and prove it. And again I'm only going to prove the first one. We're going
to do the same method. So we're going to show the left hand side is equal to the right hand side by showing that they're subsets of each other.
So first, let's suppose that X is in the left hand side. So it's in the complement of A union B. That means that X is not in A union B, so it means
that X is in neither A nor B. So I'll write that as then X is not in either A or B.
But that means that X is in the complement of A and it's in the complement of B.
X not being in A is equivalent to saying X is in the complement of A, and X
not being B is equivalent to saying X is in the complement of B.
And therefore, it's in the intersection of the complement of A and the complement of
B, because it's in both of them. So X is in A complement intersect B complement. Then we go the other way round, so now I say, conversely,
suppose that X were in the complement of A intersect complement of B.
So then that means that X is not in A, because it's in the complement, and it's not in B,
because it's in the complement of B.
So X is in neither A nor B, and that means that X is not in the union of A and B. So
not in either A or B. Then it means it's not in A union B. So I can say X
is not in A union B. i.e. X is in the complement
of that. OK.
the left hand side A union B complement is the same as the right hand side, A complement
intersect B complement. OK, and as I say, I'll leave the second one for you to have a go at, following
basically a very similar argument. OK, so these are quite important laws and they apply even if we have unions and intersections
of more than two sets. So I'll just say here that De Morgan's laws
extend to families of sets.
So if I take a union of some A Is for Is in an indexing set, and then I take the complement
of that set, that is the same as the intersection of the individual complements.
And the other way round, if I have the intersection of all the A I's and I take the complement
of that, that is the same as the union of the individual complements.
OK, so you'll make a lot of use of these laws. OK, let me summarise what we've done there,
so we've defined unions and intersections and we've seen how Venn diagrams can be a helpful way of illustrating those.
We've looked at the double inclusion principle, and seen that that's a useful way of showing that two sets are equal,
and we've used that to prove the distributive laws and then to prove De Morgan's laws.
So the next thing that we're going to look at is going to be truth tables, and these provide an alternative way of proving some of the things that we've just been looking
at. So this is truth tables. And I'll say
these provide an alternative method
for proving set identities, I'll say. OK, so how do these work. So we're going to make a table, and in the
header of the table I'm going to list some sets. And I'm going to just do two sets to
make this slightly easier. And so the way that this works is that we're going to try and catalogue all of
the possible cases for whether a given element is in each of these sets or not.
And if I work with two sets, then they're going to be four possibilities, because for each set, we could either be in or out of it.
So I'm going to fill in a bit more of this table in a second. But let me just explain how it's going to work. We're going to put in a T or an F for
true or false, in the table to catalogue
the different cases of whether a given element
is in or out of each set. And the columns are going to correspond to different sets.
So with two sets, there's going to be four possibilities, as I said. So we could be not in either A or B, in which case we put F and F, we could not be in A
but we could be in B, or we could be in A but not in B, or we could be in both of them.
And that's the four possibilities. OK, but then what we do is we can then construct other
sets. So for instance, we could look at A union B, and make another column in the table. And then we just fill it in according to whether
in each case we would be in that set. So in the first case, that's the first row,
we're not in either A or B, and therefore we're not in the union of A and B. In the
second case, we are in B and therefore we're in the union. So we would be in the union in that case. And similarly, in the third and fourth cases,
we would be in the union. OK, so that's how it works. Let's see how we could use that to prove something.
Let's prove De Morgan's laws. Again. So we can use this to prove De Morgan's laws.
And let's prove the one that we didn't prove last time. So I think that that was that the complement of the intersection of two sets is the same
as the union of their compliments. So we want to try and show that those two sets are equal to each other. So we're going
to do that by building a table. And the first part of the table is going to look identical to the one I've already drawn.
But then we're going to make the table a bit longer because I'm going to be interested in various other sets. So we're going to first of all have A and B, and I'm going to catalogue those different cases again.
So we'll have not in either of them, in b, in a, or in both of them.
And then I want to be interested in ultimately finding out whether we're in or out of this
set and this set, and the idea is that we want to try and show that these two sets are the same,
which we're going to do by showing that the columns of this table are the same. So I'm going to do this in stages. So let's, first of all, work out A intersect B, and
then we're going to work out the complement of that. You don't need to write out the all the sub stages here
if you don't want to. Then we're going to be interested in the complement of A, we're going to be interested in the complement of B,
and then we're going to be interested in the union of those two. OK, so it would have helped
if I knew what size the table was to start with.
OK, so then now for each case, I'm going to go across filling it in. So if we're not in A and we're not in B, then we're certainly not in the intersection of
A and B, and therefore we are in the complement of that. If we're not in A,
then we are in the complement of A, and we are in the complement of B (because we're not in B) and therefore we are in the union of those two.
In the second case, we're not in A and therefore we're not in the intersection of A and B,
therefore we are in the complement of that. We're not in A and therefore we are in the complement of it, but we are in B, so we're
not in the complement of C... B, sorry.
And therefore we are in the union of the two complements. OK and then we just keep going. So in the third case, we're still not in the intersection.
Therefore, we are in its complement. This time we're not in the complement of A, but we are in the complement of B, and therefore we are
still in the the union of those two complements. And in the last case, we are in the intersection of A and B and therefore we're not in the
complement. And this time, we're not in either of the complement of A or the complement of B and
therefore we're not in the union of those two complements. OK, and the point here is that this column and this column are the same.
So I'll say the fact that these two
columns are the same, shows that these two sets are equal.
So that proves this law here. OK, so that's truth tables. 
The next thing I want to talk about is cardinality of a set,
which is a measure of a set's size. I'm going to talk just about finite sets, although I'll say a word about infinite sets.
This is going to turn out to be much easier to define once we have the idea of a bijection, which is what I'm going to talk about in, I think,
two lecture's time. So I'll come back to cardinality later on. But I want to give you something to work with,
partly so that you can do a question on the problem sheet, and partly to give you practise at dealing with a slightly more awkward definition.
So we're going to look at a recursive definition for the cardinality of a finite set. At the same time, this definition is actually going to give a definition of what it means
to be a finite set, and in the end, the definition is simply going to be that the cardinality is the number of
elements in the set. But we need to explain what exactly that means. So we're going to have a definition.
So this is going to be a definition of finiteness and the cardinality for a finite set.
OK, and the definition may seem slightly peculiar to start with, but then hopefully once you've
thought about it for a while, it will make sense. So it's going to be recursive definition. So we're going to start off by saying that
the empty set is finite and has cardinality,
which we denote with kind of modulus signs around the set, zero. So the empty set has
cardinality zero. The empty set, remember, is the set with no elements. And then for any other set, I'm going to call it S,
The set S is finite and has cardinality
equal to N plus one, if there exists an element, which I'll call little S in S,
such that, if we get rid of that element from the set...
so I'm going to write that as the difference between the set S and the set that contains
just that single element S... so it's such that the cardinality of that set is n,
for some n in the natural numbers.
OK. So a set S is finite with cardinality N plus one,
if there exists an element such that getting rid of that element leaves us with a set that has cardinality N.
If that's not the case, so if it's not possible to get rid of an element and be left with something that has cardinality
that's a natural number, then the set is infinite.
So I'll say otherwise the set S is said to be infinite.
OK, so as I said, you may find that definition slightly peculiar, but if you think through
it, it is really saying that the cardinality is the number of distinct elements in the set.
So I'm going to say here that it follows that the cardinality of S is the number
of distinct elements in S. If S is finite.
Right, so you might think, well, why do we not just use that as our definition of the
cardinality? But if you think about it, that effectively is what we're saying.
We're just giving a very methodical definition of what exactly it means to say that there
are N distinct elements in the set S. Because we're saying what you should do is you should take your set and then you should
successively take elements away from it to find something that has cardinality one less,
and eventually you'll end up back with the empty set, which we know has cardinality zero.
So if you've had to take away N elements to do that, then that means that your cardinality was N.
Well, actually, the way that the definition was set up, this particular set S has got N plus one elements because we're going to have to get rid of
N plus one elements before we're left with the empty set here, which has cardinality zero. Maybe I'll just give you an example when it's kind of maybe not so totally obvious how many
elements there are in the set. So let's suppose that we take a subset of
the rational numbers, so let S be the set composed of elements M over N where M and
N are integers. So that would just be the set of rational numbers. But let's suppose that we restrict
M and N. So let me say that M and N are both greater than zero and, say, less than a million.
OK, so that set would be finite. You've got a finite number of elements, but it's not
really obvious how many it has, because the rational numbers don't have a unique way of being represented as M over
N. So a half, for instance, is One over two. But it's also two over four, and three over six, and so on.
So it's not really obvious how many different distinct elements that are here. We could work it out. But in fact that's actually what this is basically saying.
This is giving us a recipe for how we can work out how many elements there are in a
set. It's like something that maybe a computer might be able to follow. OK, so this set just
defined is finite. And it's not so obvious what its cardinality is. And to be honest, I don't know what...
I have not worked out what the cardinality of that is. If anyone wants to work it out, you can let me know.
OK, so on the problem sheet, you're going to have to prove a proposition using this
definition. So this will be a proposition. The proposition is
that we let A and B, be finite sets.
Then the cardinality of the union is equal to the sum of their individual cardinalities,
minus the cardinality of their intersection. And that's maybe something that seems obvious
if you think about the number of elements in the set, but it's something that on the problem sheet you're going to be asked to prove using this
definition, trying to kind of systematically use, a slightly awkward definition.
So I'll say proof. See the problem sheet.
This is always a cop out that the lecturer says when they don't want to bother proving something themselves!
OK, so what I'm going to do is to show you a sort of similar kind of proof of a proposition,
but a different proposition. So this is going to be a proposition to do with the number of subsets of a finite set.
So this will be subsets of a finite set.
OK, so I'm going to let A and B be finite sets,
with cardinality N. And then the proposition is that the cardinality of its power set is
two to the N. I just made it fit. So if you remember that the power set is the set of all subsets of A, and so the cardinality
of the powers set is the number of subsets of A.
And there is quite an easy way to see this, if you think about how you produce a subset of A. If A has got N elements,
then you could go through each of the N elements and decide whether you're going to put it in the subset or not.
So that's like a binary choice for each element of whether you put it in or not.
And if there's N elements that gives you two to the N different choices for whether to put the elements in or out.
And that's going to give you all of the subsets and they will be different subsets. But I want to try and show this,
just following the definition that we just gave, of what the cardinality is.
And I'm also going to make use of the proposition that we just wrote down as well.
Because the definition is recursive, it's going to be natural to try and do this by induction.
So this is the proof. And I'm going to say we use induction,
as the introduction to explain what we're doing. And so we're going to start with N
equals zero, obviously.
So if N is zero, then, well, the only set that has cardinality zero according to that definition is the empty
set. So if N is zero, then A must be the empty set.
And what is the power set of the empty set. The power set of the empty set is the empty
set itself. That's the only subset. Remember that the power set is the set of subsets, so we write that like that.
And that has cardinality one, because we can get rid of the one element and then we're
left with the empty set. So this set itself is not empty, but if we get rid of the one element that's inside it,
then it will be empty. And according to the definition, that means that this has cardinality one.
So the cardinality of the power set of the empty set is one, which is two to the power
zero, which is what it needed to be. So the proposition is true for N equals zero. So then we're going to suppose that it holds
for N. So we'll say suppose the result
holds for N, and then we're going to consider a set that has cardinality N plus one and
try and show that it holds for that. And so we're going to let A have cardinality N plus one.
So we want to try and show that the cardinality of the power set of A is two to the N plus
one. OK, so the definition, if we follow the definition of what it meant to say that A has got cardinality
N plus one, that means that we can find some element within A such that if we get rid of that element then we have something
that has cardinality N. So I need to say then there exists some A, call it little A, in A, such that, if we get
rid of this, So that's going to be A but having got rid of the set containing little A -
and I'm going to refer to this set quite a lot, so I'm going to give that a name, so I'm going to call that A primed - that's the set having got rid of little A - that
has cardinality N. OK, and so if that has cardinality N, then that's small enough such that we're supposing
the result holds for that, so we know that the continuity of the power of this A primed is going to be two to the
N. I'm going to make use of that. We want to know about the cardinality of the power set of A.
So we need to think about the subsets of A. So the subsets of A, either they're going to contain this particular element, little
A, that we got rid of, or they're not. And if they don't, then those subsets are just going to be subsets of A primed,
which are all obviously subsets of A. If they do contain the element little A,
then they're basically going to be the same, they're going to be the subsets of A primed, but then having put the element little A back in again.
So this allows us to build what we call a partition of the power set of A (I'm going
to talk about partitions in the next lecture), But I'll explain what I mean by actually just writing it down.
So we're going to split the power set of A, that's the set of all subsets, into those that contain the little A and those that don't.
So let me write some explanation of that. I'm going to say that any subset of A either
contains little A or not. So we can write (and this expression is going to be a bit
long so I'll write it on the next line), we can write the power set of A as the union of two sets.
One of them will just be the power set of A primed - that's the set of all subsets of A primed - and then the other one
so we're going to take the union of that with the other ones, which is the set of all subsets
of A primed combined with the element little A. So it's going to be a little bit awkward to write that out, so I'm going to write this
as the set... I'll just write it out and then explain it. So it's going to be a set of S union little
A, such that S is in the power set of A primed.
So if you just read that hopefully that makes sense. So this is the set of all sets that are made up of a subset
of A primed combined with the little A.
And so that's all of the possible subsets of A. So that's the power set of A. And notice that these two sets that we've split it up into
are disjoint because these ones don't contain A and these ones do contain... these ones don't contain the
little A, and these ones do contain little A, so that there's no overlap between them.
So these are disjoint and that means, according to the previous proposition, which is what you're proving on the problem sheet,
that the cardinality of this thing is just the sum of the cardinality of this thing and
the cardinality of this thing. But both of those are the same as the cardinality of this,
because the number of elements in this set here is just the same as the number of elements in this power set.
And we know both of those from the inductive hypothesis are two to the N.
So what I'm going to write here is that these two sets are disjoint,
and each has cardinality given by the cardinality of the power set
of A primed, which is two the N by the inductive hypothesis.
Hence the cardinality of the power set of a, which is the sum of those two, that's two
to the N plus two to the N, which is two to the N plus one, which is what we were trying to show.
So I can write a concluding statement here by induction, the result holds.
OK. So if we have N elements in the set, then the number of subsets of that set is two to
the N. OK, let me close by just saying a word about the cardinality of infinite sets.
This is something that we can say a bit more about once we have the idea of a bijection, and it's something that you will say more about in your analysis course later this term.
So I would just make a comment for infinite sets - it's much more interesting for infinite
sets, but a bit confusing, because this is really getting that different sizes of infinity -
I want to just make the observation that the set of natural numbers are a subset of the set of integers, which is a subset of the set of rationals, and that's
a subset of the set of reals.
So in some sense, these sets must be kind of larger than are equal to the previous ones.
it just seems like there are fewer of them - but of course there's infinitely many of
both of them, so our intuition fails us in making any kind of statement like that.
And it turns out that in terms of the cardinality of these sets, that's not true. The cardinality of the natural numbers, the integers and the rationals is
the same. So they're all in some sense, the same size sets. The cardinality of the real numbers
is larger. So anything that has the same cardinality as the natural numbers is called a countable
set, and if it's larger than that, then it's called uncountable. So I'll just say here,
but the cardinality of the natural numbers is the same as a cardinality of the integers,
and that's the same as the cardinality of the rationals. But that's less than the cardinality of the reals.
But these these these things are all nfinite cardinals, which is something that I'm not
going to go into. OK, but you will talk a bit more about this in the analysis course. OK, so let me just
summarise what we've done there. So we've seen truth tables as a way of proving set identities, we've given a recursive definition
of the cardinality for a finite set, and then we've used that to prove the number of subsets of a finite set.

Generate lecture notes in markdown format based on the provided lecture transcript. While the main content should be faithful to the transcript, feel free to elaborate on the ideas and concepts for a richer understanding, but do not introduce completely new topics or concepts. For "Homework and Assignments," "References and Resources," and "Upcoming Assessments," be very conservative about adding information and ensure these are explicitly mentioned in the transcript.

The notes should be in this format:
```markdown
## Lecture Overview

{ Summarize the main points of the lecture here }

## Detailed Lecture Summary

{ Elaborate on the points mentioned in the overview here, providing deeper context and connections where appropriate }

## Key Takeaways and Main Concepts

- { bullet list of critical points from the lecture, fleshing them out for better understanding }

## Examples/Diagrams

{ Include any examples or diagrams used during the lecture here, and explain their relevance or usefulness }

## Homework and Assignments

- { bullet list of any tasks or assignments mentioned in the lecture, do not add assignments that were not explicitly stated }

## FAQ 

{ Include questions and answers that were addressed during the lecture, and extrapolate likely questions based on the content }

Q: **{ Question }**
A: { Answer }
Q: **{ Question }**
A: { Answer }

## Glossary

- **{ Keyword }**: { Define key terms used in the lecture, adding more detail or examples for clarity }

## References and Resources

{ Mention any resources, books, or URLs mentioned during the lecture for further study. Do not add resources not explicitly stated. }

## Additional Information

{ Add other information that could help in understanding the lecture content, based on logical extensions of the material discussed }

## Upcoming Assessments

{ Note any upcoming assignments or tests mentioned in the lecture. Do not add assessments that were not explicitly stated. }

## Next Steps/Action Items

{ Summarize what the student should do next, like homework, studying certain topics, or any other tasks mentioned during the lecture }
```

ASSISTANT:
"""
    }
}

AUTH_KEY = "9EN3UDTTESKY0IO9ST54AWTUIQIHMLA784133ATC"

headers = {
    "authorization": os.getenv("RUNPOD_AI_API_KEY"),
    "accept": "application/json"
}

# Send a POST request to the /run endpoint and get the response
response = requests.post(url + "/run", json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Get the job id from the response
    job_id = response.json().get("id")
    print(f"Got job ID: {job_id}")

    # Set a flag to indicate if the job is completed or not
    completed = False

    # Loop until the job is completed
    while not completed:
        # Send a GET request to the /status endpoint with the job id as a parameter
        status_response = requests.get(url + "/status/" + job_id, headers=headers)

        # Check if the request was successful
        if status_response.status_code == 200:
            # Get the status and result from the response
            status = status_response.json().get("status")

            # Check if the status is COMPLETED
            if status == "COMPLETED":
                result = status_response.json().get("output").get("result")
                # Set the flag to True and print the result
                completed = True
                print(result)
            else:
                # Wait for 1 second before checking again
                print("Waiting for job completion...")
                time.sleep(1)
        else:
            # Print an error message and break the loop
            print("Error: Could not get the status of the job.")
            break
else:
    # Print an error message
    print("Error: Could not run the job.")
