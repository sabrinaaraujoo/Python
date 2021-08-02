'''

QUIZ EM PYTHON - N2
-
EDSON SOARES DE SOUZA      TIA:32138997
MAYARA MENEGUETTI HONDA    TIA:32152280
SABRINA DE SANTANA ARAÚJO  TIA:32108265
-
A NORMA ORTOGRÁFICA E SEU ENSINO

'''
pontos = 0
resposta = []
gabarito = []
justificativa = []

print("================ QUIZ ORTOGRÁFICO ================\n\n")
def moldePergunta(pergunta, respCerta,just):
  justificativa.append(just)
  print(pergunta)
  gabarito.append(respCerta)
  resp = input("Digite sua resposta:\n").lower()
  verific(resp)
  resposta.append(resp)


def verific(resp):
  while resp != 'a' and resp !='b' and resp !='c' and resp !='d' and resp !='e':
    resp = input("Resposta inválida, digite novamente: ").lower()



def pergunta1():
  moldePergunta('1. Ao completar os espaços com S, SS, C ou Ç, as palavras suspen_e, descan_o, licen_a, co_eira, exce_ão e an_ioso são escritas respectivamente de qual forma? \na) s, s, ç, c, ss, c\nb) s, s, ç, c, ç, s\nc) c, ç, ç, c, ç, s\nd) c, s, ç, c, s, c\ne) s, ss, s, c, ç, s', 'b', 'A reposta correta é B. Se a palavra contar com consoante precedida de vogal, nesse caso emprega-se apenas s.\nPara assumir som de /s/ entre vogais, deve-se colocar os ss\n Ç nunca pode iniciar palavras e é usado sempre antes das vogais a, o e u.\nA letra c, por sua vez, é usada sempre ante antes das vogais e e i.')
pergunta1()

def pergunta2():
  moldePergunta('\n\n2. Assinale a alternativa cujos vocábulos estão grafados corretamente e completam, respectivamente, as lacunas do texto a seguir:\n“A política de ... de gastos fez com que ... os trabalhos de ... em muitas universidades.”\na) contenção – paralizassem – pesquiza\nb) contensão – paralisassem – pesquiza\nc) contensão – paralizassem – pesquisa\nd) contenção – paralisassem – pesquisa\ne) contensão – paralizassem – pesquisa', 'd', 'A reposta correta é D. Ç nunca pode iniciar palavras e é usado sempre antes das vogais a, o e u.\nPesquisar deriva de pesquisa. Ora, se pesquisa/paralisar tem s no radical, nada mais justo que ele se mantenha no verbo.\n |s| tem som de z por estar entre vogais.')
pergunta2()

def pergunta3():
  moldePergunta('\n\n3. Na frase “... olha para a xícara fumegante...”, vê-se que a grafia correta da palavra destacada é com a letra X. Em que item a seguir há uma grafia errada?\na) enxame / mexer\nb) chuchu / chávena\nc) vexame / colcha\nd) xale / chalé\ne) engraxate / fachina', 'e', 'A reposta correta é E.\nIsso acontece, porque a palavra pode é uma forma de conjugação do verbo faxinar.')
pergunta3()

def pergunta4():
  moldePergunta('\n\n4. Extin_ão; conce_ão; suspen_ão; ob_ecar; can_ado. Para completar corretamente as palavras acima, usam-se respectivamente:\na) c - ç - s - sc – s\nb) ç – ss – s – c – s\nc) s – ss – s - sc – s\nd) s – c – s – sc – ç\ne) s – c – ç – s – ç', 'b', 'A reposta correta é B.\nO adjetivo obcecado é formado a partir do particípio do verbo obcecar, que tem sua origem na palavra em latim obcaecare, devendo assim ser escrito com c na segunda sílaba e não com s.')
pergunta4()

def pergunta5():
  moldePergunta('\n\n5. A série em que todas as palavras se escrevem com a letra x é:\na) to_a; mo_ila;\nb) en_er; en_ente;\nc) _inelo; _ocante;\nd) en_ergar; en_arcar;\ne) cai_ote; ca_umba;', 'e', 'A reposta correta é E.\ncaixote: Emprega-se o “X” depois de ditongos (encontro de duas vogais na mesma sílaba).\nCaxumba:As palavras de origem indígena e africana são habitualmente escritas com x.')
pergunta5()

def pergunta6():
  moldePergunta('\n\n6. Na ortografia da língua portuguesa, a consoante /s/ pode ser representada, na escrita, pelas letras e dígrafos seguintes: “s”, “ss”, “ç”, “c”, “sc”, “x” e “xc”, como se observa em várias palavras do texto. Assinale a alternativa em que todas as palavras estejam CORRETAMENTE grafadas.\na) Exceto, convalescença, presságio, obsceno.\nb) Extinção, consenso, extenção, realçar\nc) Submerso, auxílio, consciência, contorsão\nd) Aproximar, distorção, ranso, insosso.\ne) Abstenção, cresça, ascenção, conversão.', 'a', 'A reposta correta é A.\nExceto/Convalescença/Obsceno - A sequência xc é um dígrafo quando seguida das vogais e ou i, assumindo o valor fonético SS\nPresságio -Para que se mantenha a pronúncia s no meio das palavras, entre vogais, é necessário que se duplique a consoante s, ficando ss.')
pergunta6()

def pergunta7():
  moldePergunta('\n\n7. O x foi empregado incorretamente em:\na) enxada, feixe, ameixa\nb) enxame, enxugar, lixa\nc) xale, bruxa, mexerica\nd) xampu, xícara, graxa\ne) xaranga, xuxu, xarque', 'e', 'A reposta correta é E.\nCharanga - palavra dderivada do castelhano, Espanha.\nUtiliza-se ch em algumas palavras de origem estrangeira, como salsicha, capricho, sanduíche,… e em palavras derivadas de palavras latinas escritas com pl, cl e fl.')
pergunta7()

def pergunta8():
  moldePergunta('\n\n8. Ambas as palavras estão grafadas incorretamente em:a) capitalizar, catalizar\na) capitalizar, catalizar\nb) agonisar, batisar\nc) improvisar, anarquisar\nd) modernizar, concretizar\ne) oficializar, repizar ', 'b', 'A reposta correta é B.\nUtiliza-se o Z nos sufixos -izar.')
pergunta8()

def pergunta9():
  moldePergunta('\n\n9. Assinale a alternativa em que todos os vocábulos estejam grafados corretamente:\na) massiço, sucinto\nb) à beça, craço\nc) procissão, pretensioso\nd) assessoria, posseção\ne) improviso, concretizar', 'c', 'A reposta correta é C.\nEmprega-se ss nos substantivos terminados em “gredir”, “mitir”, “ceder” e “cutir”. Por exemplo: Progredir– progressão\nA palavra deriva de pretensão e, portanto, se escreve com "s" e não com "c".')
pergunta9()

def pergunta10():
  moldePergunta('\n\n10. Assinale a alternativa em que os vocábulos estejam grafados corretamente (S ou Z):\na) atrazo, paralizar, reprezália\nb) balisa, bazar, aprazível, frizo\nc) apoteoze, briza, gaze, griz\nd) espezinhar, cerzir, proeza, paz\ne) consumir, frazir, confessar, cazar', 'd', 'A reposta correta é D.\nEspezinhar - Nos derivados em -zal, -zeiro, -zinho, -zinha, -zito, -zita (espezinho), utiliza-se o Z.\nEtimologia (origem da palavra cerzir). Do latim sarcire, “juntar, remendar”.\nNos sufixos -ez, -eza, ao formarem substantivos abstratos a partir de adjetivos utiliza-se o Z.\Mais especificamente, a dúvida entre pás ou paz se deve ao fato de que são duas palavras homônimas homófonas, isto é, que se diferem apenas pela escrita, apresentando sons idênticos na pronúncia.')
pergunta10()


print('\n\n\n================RESULTADO================')

for i in range(10):
  if resposta[i] == gabarito[i]:
    pontos += 1
    print("\n\nA questão",i+1,'está certa!')
  else:
    pontos += 0
    print('\n\nA questão', i+1,'está errada.')
    print('A resposta correta da',i+1,'a resposta certa é:')
    print(justificativa[i])

if pontos <= 4:
  nivel = "INICIANTE"
elif pontos <= 8:
  nivel = "NTERMEDIÁRIO"
else:
  nivel = "AVANÇADO"

if pontos >= 7:
  nome = input("Digite seu nome completo para a EMISSÃO DO CERTIFICADO: \n").upper()
  print("***************CERTIFICADO***************")
  print("NOME: ",nome)
  print("NÍVEL: ",nivel)
  print("QUANTIDADE DE ACERTOS: ",pontos)
  print("*****************************************")

print("\n\nLogo sua pontuação final foi de:",pontos,"pontos e o seu nivel é: ",nivel)
print('=========================================')
