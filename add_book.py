from lib.Book import Book

privateKey="""2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d0a4d4949435777494241414b4267514335465a547a54553977706142573173396b747364326648424b3749663737585a4445377a62714d503078355938554863560a6866414a42455432564b533745654c4766496a50424d3363572f427a5a42547357496c4e6152692b5544366535394f4b73344f5a423656504e5a4b386c4357540a636e6e757972696b5857727474715043675762774e7a59494a574a784644786a4335707855304f685a6973514b592f4953384a6e36756f6554774944415141420a416f474148464e76506d56416d5337674153705442306a703866704e66556f4237633644345051755854665139613975454d4548324b56732f5252494d614c320a71794b726f46454335787748485968386e6b786333326356624237414f4b6b6f4750416e536849312f55327734726d554f503639742f62576e44387a5855675a0a3741343657314d7376586f5731632b4c65314a334555396275636c4f7042656e5a534852546d6861443750487a5745435151444e4262685148334654493774340a445a74784b576b70437649516579396b515655717165786e62667437774151456c4a706b32787479494c786d316d734d47632b7344625a37305371656d4e44790a474a696970765948416b45413578712f484c3165726e5770555453506c7770704c533065414a777569314b42453559694d2f71794e71526f42724b525253624f0a37694736636d336a41635873677a59774c624875733066526c5a53537049524465514a41416e3137533533574a6f68636b6f7933777077614a7546334a7a51580a3030506e344f6a48636b6f6e7238305a5032542b71784c754e6d696e595368686a486754796163772f4467434b494c36707259647848763671514a414c6450370a2b664d44683430466d6e6a56304a6e6236583138365a6f50454d6d336c753636735a775249777a504a435463386432555131796b34485179412f502f787256450a4d49754d546a6a37737248587370415834514a41426d3864695a536f4f6444536854675643794e6d6d50437a5a71414d512b774b7658627259575539342f6e4e0a565143304e365649676d2b5978317546784f445937374a766e5467454d42466e355176677074476431413d3d0a2d2d2d2d2d454e44205253412050524956415445204b45592d2d2d2d2d"""
objBook=Book()
print(objBook.add(privateKey=privateKey,bookName="Avunix",description="Hi book",level=3,char="0"))