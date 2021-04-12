from models import test_model

if __name__ == '__main__':
    models = [test_model]

    for model in models:
        model.run()
