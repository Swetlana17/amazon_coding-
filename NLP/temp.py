# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Data Preprocessing Template

import spacy
import pandas as pd
import spacy.displacy as displacy
import random
from spacy.util import minibatch, compounding
from spacy.training.example import Example
from pathlib import Path

nlp=spacy.load('en_core_web_md')    

train= [
              ("Account Name not populating in report.- working in qa", {"entities": [(0, 7, "FIELD"),(17,27,"ACTIVITY")]}),
              ("Submission date in incorrect format - mm/dd/yyyy - confirmed issue and code fix is required.- wrong requirement", {"entities": [(0, 10, "ACTIVITY")]}),
              ("The issue 'AUDIT DATA RECORD NOT FOUND' could not be reproduced in QA due to insufficient pre-requisites", {"entities": [(11,20, "FIELD")]}),
              ("Issues are seen with web classic trading capapbilities for PPP & CCC. Client is not able to verify trades using iFast Web, an error is displayed", {"entities": [(33,39, "ACTIVITY"),(58,60,"CLIENT"),(64,66,"CLIENT")]}),
              ("Answers Incremental Extract Job fails in XYZ SSBL_XYZ_IDR_Incremental_Extract Generation Number 8997 Job Name IFAST_ANSWERS_Incremental_Extract", {"entities": [(0,26, "JOB")]}),
              ("P0567890 - SSII - 7777 - PMMCC NCCC Rejected Trades Reporting ", {"entities": [(0,7, "PET"),(36,43,"ACTIVITY")]}),
              ("Account Name not populating in report.- working fine in QA", {"entities": [(0,7, "FIELD")]}),
              ("Broker field not populating in report - Branch name", {"entities": [(16,21, "ACTIVITY")]}),
              ("Submission date in incorrect format - mm/dd/yyyy", {"entities": [(0,14, "FIELD")]}),
              ("RDSP Account Information Screen not opening.", {"entities": [(0,23, "FIELD"),(36,42,"ACTIVITY")]}),
              ("Deactivate the BrokerControls - BCL Extract in order to get the Answers Incremental Extract file to generate without any errors.", {"entities": [(0,10, "ACTIVITY"),(33,44,"JOB")]}),
              ("PROD-SUPPORT-IFWP-BMO: RDSP Summary page shows broken", {"entities": [(18,20, "CLIENT")]}),
              ("Reference Date Prediction xml is not reporting backdated trade"),
              ("Backdated Exchange trade's EO still capturing the current NAV", {"entities": [(0,17, "ACTIVITY")]}),
              ("The response file should display the transaction type as 'PWI' and 'EDI' for InSpecies Redemption and InSpecies Purchase"),
              ("Only Specific corrections will Trigger Fixed", {"entities": [(30,36, "ACTIVITY")]}),
              ("Mismatch between the naming convention of the commission error log file in BND ", {"entities": [(0,8, "ISSUE")]}),
              ("RDSP transaction /RDSP Summary screen shows as blank.",{"entities": [(0,15, "ACTIVITY")]}),
              ("Backdated Exchange trade's EO still capturing the current NAV", {"entities": [(0,17, "ACTIVITY")]})
              ]
#train=[
      #  ("Account Name not populating in report.- working in qa",{"entities":[(0,6,"FIELD"),(18,27,"ACTIVITY")]}),
      #  ("Submission date in incorrect format - mm/dd/yyyy - confirmed issue and code fix is required.- wrong requirement",{"entities":[(0,12,"FIELD"),(18,27,"ACTIVITY")]}),
      #  ("The issue 'AUDIT DATA RECORD NOT FOUND' could not be reproduced in QA due to insufficient pre-requisites",{"entities":[(11,27,"FIELD"),(54,63,"ACTIVITY")]})
      # ]
ner=nlp.get_pipe("ner")
print(ner)
for _, annotations in train:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])
        print(ent[2])

disable_pipes =[pipe for pipe in nlp.pipe_names if pipe != 'ner']

with nlp.disable_pipes(*disable_pipes):
    optimizer = nlp.resume_training()
    for iteration in range(30):
        random.shuffle(train)
        losses={}
        
        batches=minibatch(train,size=compounding(1.0,4.0,1.001))
        for batch in batches:
            examples=[]
            for text,annotation in batch:
                examples.append(Example.from_dict(nlp.make_doc(text),annotation))
            nlp.update(examples, losses=losses, drop=0.3)
            #nlp.update(examples)
            #print(examples)
            print("Losses",losses)

for text, _ in train:
    doc = nlp(text)
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])
        
