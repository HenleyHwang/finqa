class parameters():

    prog_name = "generator"

    root_path = "../../"
    output_path = "../../output/"
    cache_dir = "../../cache/"

    op_list_file = "operation_list.txt"
    const_list_file = "constant_list.txt"

    retrieve_mode = "single"
    program_mode = "seq"

    device = "cuda"
    
    build_summary = False

    sep_attention = True
    layer_norm = True
    num_decoder_layers = 1

    max_seq_length = 512 # 2k for longformer, 512 for others
    max_program_length = 30
    n_best_size = 20
    dropout_rate = 0.1

    batch_size = 16
    batch_size_test = 16
    epoch = 20
    learning_rate = 2e-5

    report = 390
    report_loss = 100

    max_step_ind = 11
    
    ###############################################################################################
    # ## BERT generator from BERT retriever
    # model_save_name = "generator-bert-base-from-bert-base"
    # pretrained_model = "bert"
    # model_size = "bert-base-uncased"

    # train_file = root_path + "dataset/train-retrieve-bert-base.json"
    # valid_file = root_path + "dataset/dev-retrieve-bert-base.json"
    # test_file = root_path + "dataset/test-retrieve-bert-base.json"
    
    # ## Training
    # mode = "train"

    # ## Inference
    # mode = "test"
    # saved_model_path = output_path + "generator-bert-base-from-bert-base_20240506002248/saved_model/loads/20/model.pt"
    
    ###############################################################################################
    ## RoBERTa generator from BERT retriever
    model_save_name = "generator-roberta-base-from-bert-base"
    pretrained_model = "roberta"
    model_size = "roberta-base"

    train_file = root_path + "dataset/train-retrieve-bert-base.json"
    valid_file = root_path + "dataset/dev-retrieve-bert-base.json"
    test_file = root_path + "dataset/test-retrieve-bert-base.json"

    ## Training
    mode = "train"

    # ## Inference
    # mode = "test"
    # saved_model_path = output_path + "generator-roberta-base-from-bert-base_20240506114948/saved_model/loads/20/model.pt"

    ###############################################################################################
    # ## BERT generator from RoBERTa retriever
    # model_save_name = "generator-bert-base-from-roberta-base"
    # pretrained_model = "bert"
    # model_size = "bert-base-uncased"
    
    # train_file = root_path + "dataset/train-retrieve-roberta-base.json"
    # valid_file = root_path + "dataset/dev-retrieve-roberta-base.json"
    # test_file = root_path + "dataset/test-retrieve-roberta-base.json"
    
    # ## Training
    # mode = "train"

    # ## Inference
    # mode = "test"
    # saved_model_path = output_path + "generator-bert-base-from-roberta-base_20240507014907/saved_model/loads/20/model.pt"

    ###############################################################################################
    # ## RoBERTa generator from RoBERTa retriever
    # model_save_name = "generator-roberta-base-from-roberta-base"
    # pretrained_model = "roberta"
    # model_size = "roberta-base"

    # train_file = root_path + "dataset/train-retrieve-roberta-base.json"
    # valid_file = root_path + "dataset/dev-retrieve-roberta-base.json"
    # test_file = root_path + "dataset/test-retrieve-roberta-base.json"
    
    # ## Training
    # mode = "train"

    # ## Inference
    # mode = "test"
    # saved_model_path = output_path + "generator-roberta-base-from-roberta-base_20240507015008/saved_model/loads/20/model.pt"
    


    
    