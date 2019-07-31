from gensim.models.word2vec import LineSentence, Word2Vec

vec_out = "./word_vec.vector"
zhwiki_out = "./zhwiki_word"

def word2vec_train(word_path):
    print("start load words from %s" %word_path)
    sentences = LineSentence(word_path)
    print("end load words from %s, sentences max length %d" % (word_path, sentences.max_sentence_length))

    print("start trans word to vector")
    model = Word2Vec(sentences, size=200, window=5, min_count=5, workers=4)
    model.similar_by_vector
    print("end trans word to vector")

    print("start save word vector")
    model.save(vec_out)
    print("end save word vector")

if __name__== '__main__':
    word2vec_train(zhwiki_out)
