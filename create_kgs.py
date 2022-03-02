def get_entities(sent):
  ent1 = ""
  ent2 = ""
  prv_tok_dep = ""   
  prv_tok_text = ""   
  prefix = ""
  modifier = ""
  for tok in nlp(sent):
    if tok.dep_ != "punct":
      if tok.dep_ == "compound":
        prefix = tok.text
        if prv_tok_dep == "compound":
          prefix = prv_tok_text + " "+ tok.text
      if tok.dep_.endswith("mod") == True:
        modifier = tok.text
        if prv_tok_dep == "compound":
          modifier = prv_tok_text + " "+ tok.text
      if tok.dep_.find("subj") == True:
        ent1 = modifier +" "+ prefix + " "+ tok.text
        prefix = ""
        modifier = ""
        prv_tok_dep = ""
        prv_tok_text = ""      
      if tok.dep_.find("obj") == True:
        ent2 = modifier +" "+ prefix +" "+ tok.text

      prv_tok_dep = tok.dep_
      prv_tok_text = tok.text

  return [ent1.strip(), ent2.strip()]
  
def get_relation(sent):

  doc = nlp(sent)
  matcher = Matcher(nlp.vocab)
  pattern = [{'DEP':'ROOT'}, 
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},  
            {'POS':'ADJ','OP':"?"}] 
  matcher.add("matching_1", [pattern], on_match=None)
  matches = matcher(doc)
  k = len(matches) - 1
  span = doc[matches[k][1]:matches[k][2]] 

  return(span.text)
  
  
def create_graph(entity_pairs, relations):
	source = [i[0] for i in entity_pairs]
	target = [i[1] for i in entity_pairs]
	kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})
	# create a directed-graph from a dataframe
	G=nx.from_pandas_edgelist(kg_df, "source", "target", 
    edge_attr=True, create_using=nx.MultiDiGraph())
