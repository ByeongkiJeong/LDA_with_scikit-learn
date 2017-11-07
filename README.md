# LDA(Latent Dirichlet allocation) w/ sci-kit learn  
Sci-kit learn에서 LDA만 따로 쓸려고 만들었습니다.  
  
## How to import  
```Python
from LDAscikit import LDAprocess  
from LDAscikit import Utils  
```  
  
## Resources
> matplotlib==2.0.2  
> numpy==1.13.1  
> pandas==0.20.2  
> scikit_learn==0.19.1  
- You can use requirements.txt
  
## Description  
*** All data, which use in this package is based on DataFrame(pandas) ***
### LDAprocess.py  
#### Methods
> ***LDAexecute(DocWord, NumOfTopics,Verbose = 1, Max_iter = 10, TopicWordNomalization = True)***  
> Output :  DocTopic, TopicWord (Document-Topic matrix and Topic-Word matrix)  
- DocWord : Document-Word matrix(filled with Term-frequencies)  
- NumOfTopics : The number of topics  
- Verbose : Vervosity level (0, 1)  
- Max_iter : Max iteration (default  : 10)  
- TopicWordNomalization : boolean, (default : True)  
  
> ***TopicInfo(TopicWord)***  
> Output : TopicInfo (Top 10 words and probabilities for each topic)  
- TopicWord : Topic-Word matrix (Output of 'LDAexecute' method)  
  
> ***TopicDecision(DocWord, TopicNumFrom = 1, TopicNumTo = 10, CosineOrPerplexity = 0)***  
> Output : Similarity of Perplexity for each topic  
- DocWord : Document-Word matrix(filled with Term-frequencies)  
- TopicNumFrom : The number of topics to explore start (default : 1)  
- TopicNumTo : The number of topics to explore end (default : 10)  
- CosineOrPerplexity : choose between 0(Cosine similarity), 1(Perplexity), 2(Both) (default : 0)  
  
  
### Utils.py  
#### Matrix looks like below  
> |   | Term 1 | Term 2         |
> | :------------ | :-----------: | -------------------: |
> | Document 1    | (Term frequency) | (Term frequency) |
> | Document 2    | (Term frequency) | (Term frequency) |
> | Document 3    | (Term frequency) | (Term frequency) |

#### Edgelist looks like below  
> | Document | Term | Term frequency |
> | :-------- | :-------: | -----: |
> | Document 1    | Term  1 | (Term frequency) |
> | Document 2    | Term 2 | (Term frequency) |
> | Document 3    | Term 3 | (Term frequency) |

#### Methods
> ***Edgelist2Matrix(edgelist)***  
> Output : Matrix  
- edgelist : Your edgelist
  
> ***Matrix2Edgelist(matrix)***  
> Output : edgelist  
- matrix : Your matrix  
  
> ***WriteCSV(filename, matrix)***  
- filename : CSV file path to save the data 
- matrix : A DataFrame to save  
  
> ***WriteXLSX(filename, matrix)***
- filename : XLSX file path to save the data 
- matrix : A DataFrame to save  
  
> ***ReadCSV(filename, delimiter, ind_col = None)***  
> Output : pandas DataFrame  
- filename : CSV file path to read  
- delimiter : delimiter of the CSV file (such as ',', '\t', ...)  
- ind_col : Index column number(if exist) (default : None)  
  
> ***ReadXLSX(filename, ind_col = None)***  
> Output : pandas DataFrame  
- filename : XLSX file path to read  
- ind_col : Index column number(if exist) (default : None)  