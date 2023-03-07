### Feature Importances

The following table shows the feature importances for the model:

| Feature | Importance |
|---------|------------|
{% for feature, importance in feature_importances %} | {{ feature }} | {{ importance }} |
{% endfor %}

### Model Performance

The model was evaluated on {{ evaluation_data_description.num_samples }} samples, each with {{ evaluation_data_description.num_features }} features.

The following table shows the performance metrics for the model:

| Metric | Value |
|--------|-------|
{% for metric, value in performance_metrics.items() %}
| {{ metric }} | {{ value }} |
{% endfor %}

### Confusion Matrix

The following confusion matrix shows the performance of the model on the evaluation data:

![Confusion Matrix]({{ confusion_matrix_file }})

### ROC Curve

The following ROC curve shows the tradeoff between true positive rate and false positive rate for different classification thresholds:

![ROC Curve]({{ roc_curve_file }})

### Precision-Recall Curve

The following precision-recall curve shows the tradeoff between precision and recall for different classification thresholds:

![Precision-Recall Curve]({{ precision_recall_curve_file }})

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