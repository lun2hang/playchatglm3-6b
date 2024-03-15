from transformers import AutoTokenizer, pipeline, AutoModel
import torch
import bitsandbytes
import accelerate

base_model_it = "/DATA/jupyter/personal/THUDM/chatglm3-6b"

#init UI or a third part LLM API as a reward model to score a joke 



#test chatglm3 function
tokenizer = AutoTokenizer.from_pretrained(base_model_it, trust_remote_code=True)
model = AutoModel.from_pretrained(
    base_model_it,
    trust_remote_code=True).half().cuda()
model = model.eval()

instruct_init = "tell me a joke"
instruct_continue = ".good,give me another one"
gen_numer=10

instruct=instruct_init
for i in range(gen_numer):
    response, history = model.chat(tokenizer, instruct, history=[])
    print(response)
    instruct += response + instruct_continue

#init both A B model as PEFT mode for rl

#outer loop

#inner RL loop

#load all models seperatly

#all models generate a joke seperatly,using a different random seed

#reward model give all the jokes a score seperatly

#both model A B run a PPO step,and save the generation as positive sample if reward is bigger than threshhold

#inner rl loop end

#model save checkpoint
#evaluate with reward model

#A model sfted by positive sample from B, vice versa

#model save checkpoint
#eval with reward model

#end outer loop

print("end")