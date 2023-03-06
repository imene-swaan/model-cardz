# {{ model_name }}

## Model Overview

{{ model_description }}

## Intended Use

{{ intended_use }}

## Model Details

The model was created using Scikit-Learn's {{ model_algorithm }} algorithm with the following settings:

- **Number of Estimators:** {{ model_hyperparameters.n_estimators }}
- **Maximum Depth:** {{ model_hyperparameters.max_depth }}
- **Criterion:** {{ model_hyperparameters.criterion }}
- **Bootstrap:** {{ model_hyperparameters.bootstrap }}

### Preprocessing Steps

The following preprocessing steps were performed on the data prior to training the model:

{% for step in preprocessing_steps %}
- {{ step }}
{% endfor %}

### Feature Importances

The following table shows the feature importances for the model:

| Feature | Importance |
|---------|------------|
{% for feature, importance in feature_importances %}
| {{ feature }} | {{ importance }} |
{% endfor %}

### Model Performance

The model was evaluated on {{ evaluation_data_description.num_samples }} samples, each with {{ evaluation_data_description.num_features }} features.

The following table shows the performance metrics for the model:

| Metric | Value |
|--------|-------|
{% for metric, value in performance_metrics.items() %}
| {{ metric }} | {{ value }} |
{% endfor %}

### Residual Plot

The following plot shows the residuals (i.e., the difference between the predicted and actual target values) versus the predicted target values:

![Residual Plot]({{ residual_plot_file }})

### Feature Importance Plot

The following plot shows the feature importances for the model:

![Feature Importance Plot]({{ feature_importance_plot_file }})

## Data Description

The data used to train and evaluate the model consists of {{ data_description.num_samples }} samples, each with {{ data_description.num_features }} features.

### Selected Features

The following table shows the names and descriptions of the selected features:

| Feature Name | Description |
|--------------|-------------|
{% for feature, description in data_description.selected_features.items() %}
| {{ feature }} | {{ description }} |
{% endfor %}

### Data Distribution

The following plots show the distribution of the data:

{% for plot in data_distribution_plots %}
- {{ plot.title }}
![{{ plot.title }}]({{ plot.file_path }})
{% endfor %}

### Data Preprocessing Steps

The following preprocessing steps were performed on the data prior to training the model:

{% for step in data_preprocessing_steps %}
- {{ step }}
{% endfor %}
