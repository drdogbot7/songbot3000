from simpletransformers.language_generation import (
    LanguageGenerationModel,
    LanguageGenerationArgs
)

myArgs = LanguageGenerationArgs

myArgs.temperature = 1

model = LanguageGenerationModel(
    "gpt2", "bot_06082023_1827/checkpoint-8000", myArgs
)

output = model.generate("<<bst>>",None,False)

print(output)

string= output[0]

prefix="<<bst>>"
suffix="<<est>>"

# getting elements in between using split() and join()
songTitle = ''.join(string.split(prefix)[1].split(suffix)[0])

outputFile = open("output/generated.txt", "a")
outputFile.write("\n")
outputFile.write(songTitle)
outputFile.close()