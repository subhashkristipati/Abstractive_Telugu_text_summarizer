import string
import re
InputText = "పాకిస్థాన్‌తో జరిగిన మ్యాచ్‌లో అసాధారణ పోరాటంతో భారత్‌కు విజయాన్ని అందించిన విరాట్ కోహ్లి(Virat Kohli)పై ప్రపంచవ్యాప్తంగా ప్రశంసల వర్షం కురుస్తోంది. ఆఖర్లో విరాట్ చెలరేగిన తీరు చూసి మెల్‌‌బోర్న్ స్టేడియంలోని 90 వేల మంది ప్రేక్షకులు తమను తాము మర్చిపోయారు. ఆసియా కప్ ముందు వరకు రెండేళ్లకుపైగా ఫామ్ లేమితో సతమతం అయిన కోహ్లి పాకిస్థాన్‌పై తన కెరీర్లోనే బెస్ట్ అనదగ్గ ఇన్నింగ్స్‌తో మళ్లీ పునర్వైభవాన్ని అందుకున్నాడు. పాక్‌పై 53 బంతుల్లో 82 పరుగులతో నిలిచిన కోహ్లీకి టీ20 వరల్డ్ కప్‌లో ఛేజింగ్‌లో అసాధారణమైన బ్యాటింగ్ రికార్డ్ ఉంది. ఐదో టీ20 వరల్డ్ కప్ ఆడుతున్న విరాట్ కోహ్లి పొట్టి ఫార్మాట్‌ ప్రపంచ కప్‌లలో పది మ్యాచ్‌ల్లో ఛేజింగ్‌కు దిగగా 135 స్ట్రైక్ రేట్‌తో 541 పరుగులు చేశాడు. ఈ క్రమంలో కేవలం రెండు సార్లు మాత్రమే అతడు ఔట్ కావడం గమనార్హం. పాక్‌పై అజేయంగా నిలవడం ద్వారా టీ20 వరల్డ్ కప్ ఛేజింగ్‌లో అతడి సగటు 270.50కి చేరుకుంది. గతేడాది స్కాట్లాండ్‌తో జరిగిన మ్యా్చ్‌లో విరాట్ 2 పరుగులతో నాటౌట్‌గా నిలిచాడు. 2016లో నాగ్‌పూర్‌లో చేసిన 23 పరుగులే టీ20 వరల్డ్ కప్‌ లక్ష్య చేధనలో కోహ్లీకి అత్యల్ప స్కోరు కావడం గమనార్హం. 2012లో కొలంబో వేదికగా పాకిస్థాన్‌తో జరిగిన మ్యాచ్‌లో కోహ్లి 61 బంతుల్లో 78 పరుగులతో నాటౌట్‌గా నిలిచాడు. 2014లో మిర్పూర్ వేదికగా పాక్‌పైనే 36 రన్స్‌తో అజేయంగా నిలిచిన విరాట్ అదే వేదికపై అదే ఏడాది వెస్టిండీస్‌పై 54 పరుగులు చేశాడు. 2014లో మిర్పూర్‌లోనే బంగ్లాదేశ్‌పై 57 పరుగులతో, సౌతాఫ్రికాపై 44 బంతుల్లో 72 రన్స్‌తో నాటౌట్‌గా నిలిచాడు. 2016 వరల్డ్ కప్‌లో మూడు మ్యాచ్‌ల్లో టీమిండియా ఛేజింగ్‌కు దిగింది. నాగ్‌పూర్ వేదికగా న్యూజిలాండ్ జరిగిన తొలి మ్యాచ్‌లో కోహ్లి 23 పరుగులకే ఔట్ కాగా 127 పరుగుల లక్ష్య చేధనలో భారత్ 79 పరుగులకే ఆలౌటయ్యింది. కోల్‌కతా వేదికగా పాకిస్థాన్‌తో జరిగిన మ్యాచ్‌లో కోహ్లీ 37 బంతుల్లో 55 రన్స్‌తో అజేయంగా నిలిచాడు. మొహాలీ వేదికగా ఆసీస్‌తో జరిగిన క్వార్టర్ ఫైనల్ మ్యాచ్‌లో విరాట్ 51 బంతుల్లో 82 పరుగులతో నాటౌట్‌గా నిలిచి జట్టును గెలిపించాడు. దీంతో భారత్ సెమీస్ చేరుకుంది. 2021 వరల్డ్ కప్‌లో భారత్ తొలి రౌండ్లోనే నిష్క్రమించగా స్కాట్లాండ్‌పై లక్ష్య చేధనలో కోహ్లి 2 పరుగులతో నాటౌట్‌గా నిలిచాడు."
stopwords = ["పోరాటంతో", "స్టేడియంలోని",
             "బంతుల్లో", "ల్లో", "వరకు", "పై", "అదే"]


def remove_punctuations(InputText):
    regex = r"[!\"#\$%&\'\(\)\*\+,-\/:;<=>\?@\[\\\]\^_`{\|}~]"
    replaced_with = " "
    InputText = re.sub(regex, lambda m: "." if m.group(
        0) == "." else " ", InputText, 0, re.MULTILINE)
    return InputText
    # punctuations = list(string.punctuation)
    # punctuations.remove('.')
    # for i in range(len(punctuations)):
    #     InputText=InputText.replace(punctuations[i]," ")
    # return InputText


def remove_sw(sentences):
    all_words_without_sw = []
    for sentence in sentences:
        words = sentence.split(' ')
        words_without_sw = [word for word in words if not word in stopwords]
        all_words_without_sw = words_without_sw+all_words_without_sw
    for w in all_words_without_sw:
        if ((w == ' ') or (w == '')):
            all_words_without_sw.remove(w)
    return all_words_without_sw


def assign_words_tf():
    unique_words.append(tockens_without_sw[0])
    tf_unique_words.append(1)
    for i in range(len(tockens_without_sw)):
        if(i > 0):
            for j in range(len(unique_words)):
                if (tockens_without_sw[i]._eq_(unique_words[j])):
                    tf_unique_words[j] = tf_unique_words[j]+1
                    flag = 0
                    break
                else:
                    flag = 1
            if(flag == 1):
                unique_words.append(tockens_without_sw[i])
                tf_unique_words.append(1)


InputText = remove_punctuations(InputText)
InputText = InputText.replace('\u200c', '')
print('---------------------------------------------------------------------------\nInput Text\n---------------------------------------------------------------------------\n')
print(InputText)
sentences = InputText.split('. ')
print("\nTotal No. of sentences : "+str(len(sentences)))

tockens_without_sw = remove_sw(sentences)
print('---------------------------------------------------------------------------\nAll words without stop words\n---------------------------------------------------------------------------\n')
print(tockens_without_sw)
unique_words = []
tf_unique_words = []
flag = 0
assign_words_tf()
print('\n---------------------------------------------------------------------------\nWords - TF\n---------------------------------------------------------------------------\n')
for x, y in zip(unique_words, tf_unique_words):
    x = x.replace(".", "")
    print(x, y, sep='-')

MaxTF = max(tf_unique_words)
normalized_tf_unique_words = []
for i in range(len(tf_unique_words)):
    normalized_tf_unique_words.append(tf_unique_words[i]/MaxTF)

print('\n---------------------------------------------------------------------------\nWords - Normallized TF\n---------------------------------------------------------------------------\n')
for i in range(len(unique_words)):
    print(unique_words[i] + '-' + str(normalized_tf_unique_words[i]))


sentence_score = []
score = 0
for sentence in sentences:
    words = sentence.split(' ')
    for word in words:
        for j in range(len(unique_words)):
            if (word._eq_(unique_words[j])):
                score += normalized_tf_unique_words[j]
                break
            else:
                score += 0
    sentence_score.append(score)
    score = 0

for i in range(len(sentences)):
    print(sentences[i]+'----'+str(sentence_score[i])+'\n')

summary = ''
final_summary = ''
flag1 = 1
count = 4
print('---------------------------------------------------------------------------\nSentence - Score\n---------------------------------------------------------------------------\n')
while (count > 0):
    MaxValue = max(sentence_score)
    index = sentence_score.index(max(sentence_score))
    print(sentences[index]+'----'+str(sentence_score[index])+'\n')
    if(flag1 == 1):
        final_summary = sentences[index]
        flag1 = 0
    else:
        final_summary = final_summary+'. '+sentences[index]
    sentence_score.remove(MaxValue)
    count -= 1
print('---------------------------------------------------------------------------\nFinal Summary\n---------------------------------------------------------------------------\n')
print(final_summary)
