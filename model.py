from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """
You are an AI Assistant. Summarize the following youtube video transcript in the following format:
- Name of Channel: (only if it's directly mentioned like this is <name>, I'm <name> etc)
- A short title of the summary
- Main Summary in keypoints (bold important points)
- Final conclusion of the video: (if any)

{transcript}
"""

prompt = ChatPromptTemplate.from_template(template)

model =  OllamaLLM(model="deepseek-r1")

chain = prompt | model 

def summarize(transcript:str)-> str:
    return chain.invoke({f"transcript":transcript})
    
ts =  "is it possible to skip the night on 2b2t well yes if everyone on the server agrees to sleep in a bed at the same time the Knight would skip but the obvious issue is that there's always over 200 players on the server at any given time good luck trying to get them all to sleep there's got to be another way today we'll investigate whether it's really feasible to skip the night on 2bqt now we all know that 2b2t today is a very popular server with the player limit almost always being reached but before June of 2016 when the camping rusher made his first 2b2t video things were a lot different the server saw a fraction of the player counts we have today during that time it certainly would have been much more feasible to get all the players to sleep and skip the night especially when you're the only player online as seen in this famous screenshot taken by fit MC so during that time it was extremely likely that players did successfully skip the night on 2b2t to no Fanfare but once June 1st 2016 hit 2b2t was almost always pegged at its max player limit at this point you couldn't just convince hundreds of players on a toxic Anarchy server to either all sleep log off or go to the nether just to skip the night there was literally no practical way at all to even consider accomplishing this feat 2b2t would never see a night skip again until five years later the exact date was June 18 2021 it was a normal day on 2b2t until it suddenly started lagging immensely likely due to a DDOS attack everyone on the server got disconnected except for a few players that were a part of the spawn Masons they normally kept a few accounts online at any given time to gain easy access to the server but these accounts were connected to 2b2t in such a way that they were not affected by the DDOS and were still able to play normally like nothing ever happened so when they eventually realized their unique situation they quickly disconnected a few of their accounts leaving five or so online to all sleep in a bed being the first players to successfully skip the night on 2b2t in half a decade absolutely no prior planning for this was made it was just a matter of luck and extremely quick planning after all there was only a 20 minute window for this feat to be accomplished because after that that the rest of the players online were kicked so will we ever witness another night skip on 2b2t I'm not sure but given how unlikely this event was I wouldn't bet on it happening again anytime soon [Music]"

if __name__ == "__main__":
    print(summarize(ts).split("</think>")[-1])