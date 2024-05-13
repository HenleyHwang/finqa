# FinQA
This project develops a question answering system focused on financial documents, utilizing Natural Language Processing (NLP) with a Transformer-based model.
In this context, financial question answering (FinQA) entails automatically generating answers to queries through numerical reasoning, providing insightful analysis of financial data.

## Requirements

- pytorch 2.2.0
- huggingface transformers 4.40.1

## Dataset
Download the dataset from https://github.com/czyssrs/FinQA/tree/main/dataset.

## Retriever
Go to folder "code/retriever".

### Train
To train the retriever, edit config.py to set your own project and data path. Set "model_save_name" to the name of the folder you want to save the checkpoints. You can also set other parameters here. Then run:

```
python Main.py
```

### Inference
To run inference, edit config.py to change "mode" to "test", "saved_model_path" to the path of your selected checkpoint in the training, and "model_save_name" to the name of the folder to save the result files. Then run:

```
python Test.py
```

It will create an inference folder in the output directory and generate the files used for the program generator.

To train the program generator in the next step, we need to get the retriever inference results for all the train, dev, and test files. Edit config.py to set "test_file" as the path to the train file, dev file, and test file respectively, also set "model_save_name" correspondingly, and run Test.py to generate the results for all 3 of them.

## Generator
Go to folder "code/generator".

### Train
First we need to convert the results from the retriever to the files used for training. Edit the main entry in Convert.py to set the file paths to the retriever results path you specified in the previous step - for all 3 train, dev, and test files. Then run:

```
python Convert.py
```

to generate the train, dev, test files for the generator.

Edit other parameters in config.py, like your project path, data path, the saved model name, etc. To train the generator, run:

```
python Main.py
```

### Inference
To run inference, edit config.py to change "mode" to "test", "saved_model_path" to the path of your selected checkpoint in the training, and "model_save_name" to the name of the folder to save the result files. Then run:

```
python Test.py
```

It will generate the result files in the created folder.

## References
1. Chen, Z.; Chen, W.; Smiley, C.; Shah, S.; Borova, I.; Langdon, D.; Moussa, R.; Beane, M.; Huang, T.-H.; Routledge, B.; and Wang, W. Y. 2021. FinQA: A Dataset of Numerical Reasoning over Financial Data. Proceedings of EMNLP 2021. https://github.com/czyssrs/FinQA.
