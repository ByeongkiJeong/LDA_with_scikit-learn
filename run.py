from LDAscikit import LDAprocess
from LDAscikit import Utils

df_matrix = Utils.ReadCSV(filename = "matrix.csv", delimiter = ',', ind_col = 0)
DocTopic, TopicWord = LDAprocess.LDAexecute(df_matrix, 23,1,20)
TopicInfo = LDAprocess.TopicInfo(TopicWord)
similarity = LDAprocess.TopicDecision(df_matrix, TopicNumFrom = 2, TopicNumTo = 100, CosineOrPerplexity = 2)

Utils.WriteXLSX("DocTopic.xlsx", DocTopic)
Utils.WriteXLSX("TopicWord.xlsx", TopicWord)
Utils.WriteXLSX("TopicInfo.xlsx", TopicInfo)