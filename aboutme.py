from nltk.corpus import wordnet

def lambda_handler(event=None, context=None):
    cat = wordnet.morphy('cats')
    print('morphy result', cat)
    
    bag = 'hello world'
    return {
        "statusCode": 200,
        "body": cat
    }