import argparse
import fasttext

parser  = argparse.ArgumentParser(description="Generate synonyms for a word file.")
general = parser.add_argument_group("general")
general.add_argument("--model"    , default="/workspace/datasets/fasttext/normalized_title_model.bin", help="model file location")
general.add_argument("--threshold", default=0.7, help="similarity threshold")
general.add_argument("--input"    , default="/workspace/datasets/fasttext/top_words.txt", help="top words file location")
general.add_argument("--output"   , default="/workspace/datasets/fasttext/synonyms.csv", help="synonyms (results) file location")

if __name__ == "__main__":

    args       = parser.parse_args()
    modelFile  = args.model
    threshold  = args.threshold
    inputFile = args.input
    outputFile = args.output

    input_file = open(args.input)
    top_words = input_file.readlines()

    model = fasttext.load_model(modelFile)

    with open(inputFile, "r") as topWords:
        with open(outputFile, "w") as output:

            for word in topWords:
                word = word.strip()
                entry = word

                synonyms = model.get_nearest_neighbors(word)

                for synonym in synonyms:
                    if float(synonym[0]) > threshold:
                        entry += f", {synonym[1]}"
                    
                output.write(f"{entry},\n")
