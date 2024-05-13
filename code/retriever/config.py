class parameters():

    prog_name = "retriever"

    root_path = "../../"
    output_path = "../../output/"
    cache_dir = "../../cache/"

    train_file = root_path + "dataset/train.json"
    valid_file = root_path + "dataset/dev.json"
    test_file = root_path + "dataset/test.json"

    op_list_file = "operation_list.txt"
    const_list_file = "constant_list.txt"
  
    resume_model_path = ""
    
    device = "cuda"

    build_summary = False

    option = "rand"
    neg_rate = 3
    topn = 5

    sep_attention = True
    layer_norm = True
    num_decoder_layers = 1

    max_seq_length = 512
    max_program_length = 100
    n_best_size = 20
    dropout_rate = 0.1

    batch_size = 16
    batch_size_test = 16
    epoch = 20
    learning_rate = 2e-5

    report = 2672
    report_loss = 100

    ###############################################################################################
    ## BERT retriever
    model_save_name = "retriever-bert-base"
    model_size = "bert-base-uncased"
    pretrained_model = "bert"

    ## Training
    mode = "train"

    # ## Inference for generator
    # mode = "test"
    # saved_model_path = output_path + \
    #     "retriever-bert-base_20240505142203/saved_model/loads/20/model.pt"

    # model_save_name = model_save_name + "-inference-train"
    # test_file = root_path + "dataset/train.json"
    
    # model_save_name = model_save_name + "-inference-dev"
    # test_file = root_path + "dataset/dev.json"
    
    # model_save_name = model_save_name + "-inference-test"
    # test_file = root_path + "dataset/test.json"
    
    ###############################################################################################
    # ## RoBERTa retriever
    # model_save_name = "retriever-roberta-base"
    # pretrained_model = "roberta"
    # model_size = "roberta-base"

    # ## Training
    # mode = "train"

    # ## Inference for generator
    # mode = "test"
    # saved_model_path = output_path + \
    #     "retriever-roberta-base_20240506161410/saved_model/loads/20/model.pt"

    # model_save_name = model_save_name + "-inference-train"
    # test_file = root_path + "dataset/train.json"
    
    # model_save_name = model_save_name + "-inference-dev"
    # test_file = root_path + "dataset/dev.json"
    
    # model_save_name = model_save_name + "-inference-test"
    # test_file = root_path + "dataset/test.json"
