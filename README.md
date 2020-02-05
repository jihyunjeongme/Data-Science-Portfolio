

<h1 align="center">
  <br>
  <img src="https://user-images.githubusercontent.com/43984584/73836988-d4ecde00-4853-11ea-97d8-6089b597b0f1.png" alt="" width=""></a>
  <br>
  
  <br>
</h1>

<h1 align="center">Data Science Portfolio
</p>

## Contents
- Programming(Analysis) Skills
    - Anaconda
    - Jupyter notebook
    - Python
    - Numpy
    - Pandas
    - Matplotlib

- SL(Statistical Learning)
<img src="https://user-images.githubusercontent.com/43984584/73838510-2ea2d780-4857-11ea-9c3b-74808de00b22.png">
```
    Supervised learning: Prediction(예측)
    - t-test: 일표본, 독립, 쌍, 비모수
    - ANOVA: ANOVA, MANOVA, ANCOVA, MANCOVA
    - 단순 선형 회귀
    - 다중 선형 회귀
    - Timeseries 
        - Practice(실습): Pre류diction for the stock price of Samsung electronics(삼성전자 주식 가격을 예측해보자)
```
```
    Supervised learning: Classification(분류)
    - 카이 제곱 검정
    - 로지스틱 회귀
    - K - 최근 접 이웃(KNN)
    - SVM
    - 선형 판별 분석(LDA)
    - 분류 방법의 비교 
```
```
    Unsupervised learning: 
    - 그룹화(Grouping)
    - 파티션 클러스터링(k 평균 클러스터링)
    - 계층적 클러스터링
    - 차원 축소(Dimensino reduction)
        - 차원의 저주
        - 요인 분석: EFA 및 CFA
    - 주요 성분 분석 (PCA)
    - 부분 최소 제곱 (PLS)
    - 확인 요인 분석 (CFA)
    - 독립 성분 분석 (ICA)
    - MDS (Multi-Dimensional Scalling)
```
- ML(Machine learning)
    - Scikit-learn
    
- DL(Deep learning)
    - LSTM
    - DNN
    - CNN
    
- Supervised learning 
- Unsupervised learning

## 대상자

- 어느정도 파이썬 문법중 변수, 함수, 리스트, 반복문, 조건문 등 기초적인 지식은 알고 있다는 전제로 진행합니다.

### Step 1 - Data

- JSON 파일에 대해서 간단히 알아보고 넘어가도록 합시다
- [자세히 알아보기](https://developers.squarespace.com/what-is-json/)
- 아래의 소스 코드를 작성합니다. 그리고 `dictionary.json`을 다운 받습니다.
- 실행해봅시다.

```bash
#Import library
import json

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two line of this snippet
data = json.load(open("dictionary.json"))

#Function for retriving definition
def retrive_definition(word):
    return data[word]

#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
print(retrive_definition(word_user))
```

### Step 2 - Check for non-existing words

- `dictionary.json` 사전에 해당 단어가 있는지 없는 지 체크하는 로직을 추가 해 줍니다.
- 추가 된 소스

```bash
#Import library
import json

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two line of this snippet
data = json.load(open("dictionary.json"))

#Function for retriving definition
def retrive_definition(word):
    #Check for non existing words
    if word in data:
        return data[word]
    else:
        return ("The word doesn't exist, please double check it.")

#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
print(retrive_definition(word_user))
```

### Step 3 - The case-sensitivity

- 입력된 값이 대문자, 소문자, 그리고 첫글자 대문자 인 경우를 고려하여 조건문(if,elif)을 추가합니다.

- 고려될 내용

  - Case 1 — To make sure the program returns the definition of words that start with a capital letter (e.g. Delhi, Texas) we will also check for the title case letters in else-if condition.

  - Case 2 — To make sure the program returns the definition of acronyms (e.g. USA, NATO) we will check for the uppercase as well.

- 추가된 코드

```bash
#Import library
import json

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two line of this snippet
data = json.load(open("dictionary.json"))

#Function for retriving definition
def retrive_definition(word):
    #Removing the case-sensitivity from the program
    #For example 'Rain' and 'rain' will give same output
    #Converting all letters to lower because out data is in that format
    word = word.lower()

    #Check for non existing words
    #1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
    #2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]

#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
print(retrive_definition(word_user))
```

### Step 4 — Closest Match

- 구글 검색을 하다보면 아래와 같이 오타를 입력해도 유사한 결과 값을 대신해서 보여줍니다.
- 우리 사전에도 해당 기능을 추가해봅시다.

<img src = "https://cdn-images-1.medium.com/max/2600/1*dLzW8P3sVDiMfna6XP1Gzg.png" width = "" height=""></img>

- 해당 기능을 익히기 위해서는 파이썬 `difflib` 라이브러리가 필요합니다.
- 해당 기능을 위해서는 2가지 방법을 익혀야 합니다.(나는 완료 소스코드만 이해하면 된다는 분은 해당 내요을 건너띄고 다시 와서 확인 하면 됩니다.)

- Method 1 — Sequence Matcher
  > Let’s understand this method. First, we will import the library and fetch method from it. The SequenceMatcher() function takes total 3 parameters. First one is junk, which means if the word has white spaces or blank lines, in our case that’s none. Second and third parameters are the words between which you want to find similarities. And appended ratio method will give you the result in the number.

* 소스코드

```bash
    #Import library
import json
# This is a python library for 'Text Processing Serveices', as the offcial site suggests.
import difflib
from difflib import SequenceMatcher

#Let's load the same data again
data = json.load(open("dictionary.json"))

#Run a Sequence Matcher
#First parameter is 'Junk' which includes white spaces, blank lines and so onself.
#Second and third parameters are the words you want to find similarities in-between.
#Ratio is used to find how close those two words are in numerical terms
value = SequenceMatcher(None, "rainn", "rain").ratio()

#Print out the value
print(value)
```

- Method 2 — Get Close Matches

  > The method works as follows, the first parameter is, of course, the word for which you want to find close matches. The second parameter is a list of words to match against. The third one indicates how many matches do you want as an output. And the last one is cut off. Do you remember we got a number in the previous method? 0.89? Cutoff uses that number to know when to stop considering a word as a close match (0.99 being the closest to the word). You can set that according to your criteria.

* 소스코드

```bash
#Import library
import json
# This is a python library for 'Text Processing Serveices', as the offcial site suggests.
import difflib
from difflib import get_close_matches

#Let's load the same data again
data = json.load(open("dictionary.json"))

#Before you dive in, the basic template of this function is as follows
#get_close_matches(word, posibilities, n=3, cutoff=0.66)
#First parameter is of course the word for which you want to find close matches
#Second is a list of sequences against which to match the word
#[optional]Third is maximum number of close matches
#[optional]where to stop considering a word as a match (0.99 being the closest to word while 0.0 being otherwise)

output = get_close_matches("rain", ["help","mate","rainy"], n=1, cutoff = 0.75)

# Print out output, any guesses?
print(output)
```

- 직접 실습해보면서 두 가지 기능에 대해서 충분히 이해했을 거라 생각합니다.

### Step 5 — Did you mean this instead?

- 이번에는 입력된 값이 오타 일 경우 가장 유사한 단어를 찾아서 리턴을 한번 해보겠습니다.

- 아래 소스코드를 추가합니다.

```bash
#Check for non existing words
#1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
#2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
if word in data:
    return data[word]
elif word.title() in data:
    return data[word.title()]
elif word.upper() in data:
    return data[word.upper()]
#3rd elif: To find a similar word
#-- len > 0 because we can print only when the word has 1 or more close matches
#-- In the return statement, the last [0] represents the first element from the list of close matches
elif len(get_close_matches(word, data.keys())) > 0:
    return ("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
```

### Step 6 — Retrieving the definition

- 마지막으로 오타가 발생했을 때 가장 유사 단어를 찾아 준 다음 Y or N를 질문한 뒤에 로직을 처리 합니다.
- 아래의 소스 코드를 추가합니다.

```bash
elif len(get_close_matches(word, data.keys())) > 0:
    action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
    #-- If the answers is yes, retrive definition of suggested word
    if (action == "y"):
        return data[get_close_matches(word, data.keys())[0]]
    elif (action == "n"):
        return ("The word doesn't exist, yet.")
    else:
        return ("We don't understand your entry. Apologies.")
```

### Step 7 — The Icing on the cake

- 마지막으로 여러 줄로 출력 되었던 단어의 정의를 한줄씩 잘라서 출력해보겠습니다.
- 소스코드

```bash
#Retrive the definition using function and print the result
output = retrive_definition(word_user)

#If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-",item)
#For words having single definition
else:
    print("-",output)
```

## 최종 소스코드 - `dictionary.py`

```bash
# Import library
import json

# This is a python library for 'Text Processing Services', as the official site suggests.
# Loading the json data as python dictionary
from difflib import get_close_matches

# Loading the json data as python dictionary
# Try typing "type(data)" in terminal after executing first two line of this snippet
data = json.load(open("dictionary.json"))

# Function for retriving definition


def retrive_definition(word):

    # Removing the case-sensitivity from the program
    # For example 'Rain' and 'rain' will give same output
    # Converting all letters to lower because out data is in that format

    word = word.lower()

    # Check for non existing words
    # 1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
    # 2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
    # 3rd elif: To find a similar word
    # -- len > 0 because we can print only when the word has 1 or more close matches
    # -- In the return statement, the last [0] represents the first element from the list of close matches

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [Y or N]: " % get_close_matches(
            word, data.keys())[0])

        if (action == "Y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "N"):
            return ("The word doesn't exist, yet")
        else:
            return ("We don't understand your entry. Apologies.")


# Input from user
word_user = input("Enter a word: ")

# Retrive the definition using function and print the result
output = retrive_definition(word_user)

# If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-", item)

# For words having single definition
else:
    print("-", output)

```

## 기타

- 한글로 만들어진 단어사전으로 추가 실습을 해보면 유용한 기능으로 생각됩니다.
