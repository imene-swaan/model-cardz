# {{ title }}

##### {{ subtitle }}


## Intended Use

{{ intended_use }}


## Model Overview

{{ model_description }}


## Model Details

The model was created using Scikit-Learn's {{ model_name }} algorithm with the following hyperparameters:

| Hyperparameter | value | Default |
|:--------------:|:-----:|:-------:|
{% for param, val in model_params.items() %}| **{{ param }}**| {{ val[0] }} | {{ val[1] }} | 
{% endfor %}


A short description of the hyperparameters of the {{ model_name }} model:
{% for param in model_params_description %}
- {{ param }}
{% endfor %}

### Feature Importances

The following table shows the feature importances for the model:

| Feature | Importance |
|:-------:|:----------:| 
{% for feature, importance in feature_importance.items() %} | {{ feature }} | {{ importance }} |
{% endfor %}


The following Bar Plot shows the feature importances for the model:

![Feature Importances]({{ feature_importance_plot }})