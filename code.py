from sklearn.metrics import roc_auc_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

spam_data = pd.read_csv('spam.csv')

spam_data['target'] = np.where(spam_data['target'] == 'spam', 1, 0)


X_train, X_test, y_train, y_test = train_test_split(spam_data['text'],
                                                    spam_data['target'],
                                                    random_state=0)


def answer_one():

    num_of_spam_entries = len(spam_data[spam_data['target'] == 1])
    spam_percentage = 100 * (num_of_spam_entries/len(spam_data))
    return spam_percentage


# print(answer_one())


def answer_two():

    vect = CountVectorizer().fit(X_train)
    longest_token = max(vect.get_feature_names(), key=len)
    return longest_token


# print(answer_two())


def answer_three():

    count_vect = CountVectorizer().fit(X_train)
    count_vect_transformed = count_vect.transform(X_train)
    model = MultinomialNB(alpha=0.1).fit(count_vect_transformed, y_train)
    # Predict the transformed test documents
    predictions = model.predict(count_vect.transform(X_test))

    auc = roc_auc_score(y_test, predictions)
    return auc


print(answer_three())
