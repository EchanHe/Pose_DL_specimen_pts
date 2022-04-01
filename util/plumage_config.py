import configparser
from datetime import date
def process_config(conf_file):
    """
    Read the config file into dictionary
    """
    params = {}
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    print('Read config file : ' , conf_file,"\n")
    config.read(conf_file)
    for section in config.sections():
        if section == 'Directory':
            for option in config.options(section):
                params[option] = config.get(section, option)
        if section == 'DataSet':
            for option in config.options(section):
                params[option] = eval(config.get(section, option))
        if section == 'Network':
            for option in config.options(section):
                params[option] = eval(config.get(section, option))
        if section == 'Train':
            for option in config.options(section):
                params[option] = eval(config.get(section, option))
        if section == 'Summary':
            for option in config.options(section):
                params[option] = eval(config.get(section, option))
        if section == 'Saver':
            for option in config.options(section):
                params[option] = eval(config.get(section, option))
    return params


def generate_grid_params(params):
    """
    Decide whether a config has list param, so it is used for grid search.

    Return a dictionary with {Name: value parameters}
    """
    # The keys can be used as grid search.
    keys = ['scale' , 'is_grey' , 'img_aug',
        'learning_rate','learning_rate_decay', 'exponential_decay_epoch',
        'decay_restart', 'first_decay_epoch', 'optimizer',
        'batch_size', 'l2','dropout_rate', 
        'nlow','nstacks','output_stride','split_seed','kfold']
    grid_params = {}

    for key in keys:
        if key in params.keys():
            if isinstance(params[key] ,list):
                grid_params[key] = params[key]

    return grid_params

def extract_config_name(params):
    keys = ['category', 'nepochs','network_name', 'nstacks', 'scale' , 'is_grey' , 'img_aug',
        'learning_rate','batch_size', 'optimizer', 'decay_restart','split_seed','kfold']

    simple_keys = {'category':'v','nepochs':'epo','network_name':'net', 'scale':'sca' , 'is_grey':'grey' ,
     'img_aug': 'aug', 'learning_rate':'lr','batch_size':'bat', 'optimizer':'opt', 
     'decay_restart':'restart','split_seed':'seed' , 'kfold':'kf','nstacks':'stk'}

    simple_values = {'cpm_vgg':'cpm','hourglass':'HG' , 'False':'F' , 'True':'T'}

    params['config_name'] = ""
    for key in keys:
        if key in params.keys():
            v = str(params[key])
            if v in simple_values:
                params['config_name'] += "{}-{};".format(simple_keys[key],simple_values[v]) 
            else:
                params['config_name'] += "{}-{};".format(simple_keys[key],v) 
    params['config_name'] = str(date.today())+"_"+params['config_name']


def config_training_steps(params , training_set_size):
    """
    Goal: set the steps in training process from config file
    """
    one_epoch_steps = training_set_size//params['batch_size']
    params["training_set_size"] = training_set_size
    params["one_epoch_steps"] = one_epoch_steps
    params["total_steps"] = params['nepochs'] * params["one_epoch_steps"]
    params["summary_steps"] =  params["total_steps"]  // params['summary_interval']
    params["valid_steps"] = params["total_steps"] // params['valid_interval']
    params["saver_steps"] = params["total_steps"] // params['saver_interval']
    print('Total steps: {}\nOne epoch: {}\nSum steps: {}, Valid steps: {}, Save steps: {}'.format(params["total_steps"],
        params["one_epoch_steps"],params["summary_steps"],params["valid_steps"],params["saver_steps"]))


# def training_network(prediction , loss , train_op, sess,config):
def _help_func_dict(config,key, default_value = None):
    if key in config:
        return config[key]
    else:
        return default_value

