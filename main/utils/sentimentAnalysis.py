from googleapiclient import discovery
import os

from dotenv import load_dotenv
load_dotenv()

import openai

openai.api_key = os.getenv("OPEN_AI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

google_client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=GOOGLE_API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

def getPerspectiveScore(text):
    analyze_request = {
        'comment': { 'text': str(text) },
        'requestedAttributes': {'TOXICITY': {}, 'SEVERE_TOXICITY': {}, 'PROFANITY': {}, 'THREAT': {}, 'INSULT': {}, 'IDENTITY_ATTACK': {}}
    }
    
    response = google_client.comments().analyze(body=analyze_request).execute()
    return(
      (0.7*response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]) + 
      (response["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"]) + 
      (0.5*response["attributeScores"]["PROFANITY"]["summaryScore"]["value"]) + 
      (response["attributeScores"]["THREAT"]["summaryScore"]["value"]) + 
      (0.8*response["attributeScores"]["INSULT"]["summaryScore"]["value"]) + 
      (response["attributeScores"]["TOXICITY"]["summaryScore"]["value"])
      )
      
def getGPTScore(text):

  completions = openai.Completion.create(
      engine='text-davinci-003',
      temperature=0.5, 
      prompt=f'Imagine you are tasked with being the greatest sentiment analyzer ever. You are given the ability to analyze text in more depth than anything before you. Decide how hostile and threatening a comment is from a scale of 0.0 to 1.0.\nContext: This is a conversation between a rideshare driver and passanger. The expected tone is professional and friendly. Keep this in mind while giving your answer.\n\nExamples:\nText: \"You suck at driving\"\nRating: 0.7314\n\nText: \"You are so good at driving\"\nRating: 0.1343\n\nText: \"Are you stupid?\"\nRating: 0.8648\n\nText:\"{text}\"\nRating:',
      max_tokens = 3,
      n=1
  )

  return float(completions["choices"][0]["text"].strip())