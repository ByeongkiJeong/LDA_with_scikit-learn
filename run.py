from LDAscikit import LDAprocess
from LDAscikit import Utils

df_matrix = Utils.ReadCSV("matrix.csv", ',', 0)
DocTopic, TopicWord = LDAprocess.LDAexecute(df_matrix, 2,1,1)
TopicInfo = LDAprocess.TopicInfo(TopicWord)
LDAProcess.TopicDecision(df_matrix, TopicNumFrom = 2, TopicNumTo = 2, CosineOrPerplexity = 0)