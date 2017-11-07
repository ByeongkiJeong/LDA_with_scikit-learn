from LDAscikit.LDAprocess import LDAprocess
from LDAscikit.Utils import Utils

df_matrix = Utils().ReadCSV(filename = "matrix.csv", delimiter = ',', ind_col = 0)
#DocTopic, TopicWord = LDAprocess.LDAexecute(df_matrix, 2,1,1)
#TopicInfo = LDAprocess.TopicInfo(TopicWord)
similarity = LDAprocess().TopicDecision(df_matrix, TopicNumFrom = 2, TopicNumTo = 100, CosineOrPerplexity = 0)
print(similarity)