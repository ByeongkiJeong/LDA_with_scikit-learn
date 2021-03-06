import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity

def LDAexecute(DocWord, NumOfTopics,Verbose = 1, Max_iter = 10, TopicWordNomalization = True):
    LDAmodule = LatentDirichletAllocation(n_components=NumOfTopics, doc_topic_prior=None, topic_word_prior=None, learning_method='batch', 
                                        learning_decay=0.7, learning_offset=10.0, max_iter=Max_iter, batch_size=128, evaluate_every=1, 
                                        total_samples=1000000.0, perp_tol=0.1, mean_change_tol=0.001, max_doc_update_iter=100, 
                                        n_jobs=1, verbose = Verbose, random_state=None)

    data = LDAmodule.fit_transform(DocWord)
    topic_names = ["Topic%i"% i for i in range(1, NumOfTopics + 1)]
    DocTopic = pd.DataFrame(data, columns = topic_names, index = DocWord.index)
    if TopicWordNomalization:
        TopicWord = pd.DataFrame(LDAmodule.components_ / LDAmodule.components_.sum(axis=1)[:, np.newaxis], columns = DocWord.columns, index = topic_names)
    else:
        TopicWord = pd.DataFrame(LDAmodule.components_, columns = DocWord.columns, index = topic_names)
    return DocTopic, TopicWord

def TopicInfo(TopicWord):
    list_temp = []
    for _, row in TopicWord.iterrows():
        temp = row.sort_values(ascending = False).iloc[0:20]
        temp_row = [temp.index[0], temp.iloc[0], temp.index[1], temp.iloc[1], temp.index[2], temp.iloc[2], temp.index[3], temp.iloc[3], temp.index[4], temp.iloc[4],
                    temp.index[5], temp.iloc[5], temp.index[6], temp.iloc[6], temp.index[7], temp.iloc[7], temp.index[8], temp.iloc[8], temp.index[9], temp.iloc[9],
                    temp.index[10], temp.iloc[10], temp.index[11], temp.iloc[11], temp.index[12], temp.iloc[12], temp.index[13], temp.iloc[13], temp.index[14], temp.iloc[14],
                    temp.index[15], temp.iloc[15], temp.index[16], temp.iloc[16], temp.index[17], temp.iloc[17], temp.index[18], temp.iloc[18], temp.index[19], temp.iloc[19]]
        list_temp.append(temp_row)
    TopicInfo = pd.DataFrame(data=list_temp, columns=['1stWord','1stProb','2ndWord','2ndProb','3rdWord','3rdProb','4thWord','4thProb','5thWord','5thProb',
                                                      '6thWord','6thProb','7thWord','7thProb','8thWord','8thProb','9thWord','9thProb','10thWord','10thProb',
                                                      '11stWord','11stProb','12ndWord','12ndProb','13rdWord','13rdProb','14thWord','14thProb','15thWord','15thProb',
                                                      '16thWord','16thProb','17thWord','17thProb','18thWord','18thProb','19thWord','19thProb','20thWord','20thProb'], index=TopicWord.index)
    return TopicInfo

def TopicDecision(DocWord, TopicNumFrom = 1, TopicNumTo = 10, StepSize=1, CosineOrPerplexity = 0):
    """Return DataFrame of cosine similarity or perplexity"""
    LDAprocesses = []
    TopicNum = [TopicNumFrom]
    if StepSize == 1:
        TopicNum = list(range(TopicNumFrom, TopicNumTo+1))
    else:
        temp = TopicNumFrom
        while temp < TopicNumTo:
            temp = temp + StepSize
            TopicNum.append(temp)
    for i in TopicNum:
        print("Processing NumOfTopic: %i"%i)
        LDAprocesses.append(LatentDirichletAllocation(n_components=i, learning_method='batch', max_iter=10).fit(DocWord))
    if CosineOrPerplexity == 0:
        list_similarity = []
        for i in LDAprocesses:
            temp_TopicWord = i.components_ / i.components_.sum(axis=1)[:, np.newaxis]
            list_similarity.append(np.average(cosine_similarity(X = temp_TopicWord, Y = None)))
        plt.plot(TopicNum, list_similarity)
        plt.ylabel('Avg cosine similarity')
        plt.xlabel('# of Topics')
        plt.show()
        return pd.DataFrame(list_similarity, index=TopicNum, columns=["avg cosine sim"])
    elif CosineOrPerplexity == 1:
        list_perplexity = []
        for i in LDAprocesses:
            list_perplexity.append(i.perplexity(DocWord, sub_sampling=True))
        plt.plot(TopicNum, list_perplexity)
        plt.ylabel('Perplexity')
        plt.xlabel('# of Topics')
        plt.show()
        return pd.DataFrame(list_perplexity, index=TopicNum, columns=["perplexity"])
    elif CosineOrPerplexity == 2:
        list_similarity = []
        for i in LDAprocesses:
            temp_TopicWord = i.components_ / i.components_.sum(axis=1)[:, np.newaxis]
            list_similarity.append(np.average(cosine_similarity(X = temp_TopicWord, Y = None)))
        list_perplexity = []
        for i in LDAprocesses:
            list_perplexity.append(i.perplexity(DocWord, sub_sampling=True))
        return pd.concat([pd.DataFrame(list_similarity, index=TopicNum, columns=["avg cosine sim"]), pd.DataFrame(list_perplexity, index=TopicNum, columns=["perplexity"])], axis=1)

if __name__ == "__main__":
    df_matrix = pd.read_csv('matrix.csv', delimiter=',', index_col=0)
    DocTopic, TopicWord = LDAexecute(df_matrix, 2,1,1)