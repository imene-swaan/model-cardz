{# templates/markdown.txt #}

<h1 align="center"> {{title}} </h1>

<h3 align="center"> {{subtitle}} </h3>

<h5 align="center"> {{description}} </h5>



## The DATA
##
### Training Data:
  
  {% if model == 'regression' %}
- The target variable is **{{ type_y_train }}** with mean **{{ mean_y_train}}** and standard deviation **{{ std_y_train}}**. 
  

  {% elif model == 'classification' %}
- there are {{ number_classes }} classes in this classification task.
  
  {% elif model == 'Unkown model' %}
- Unkown model. Unable to generate insight!


{% else %}
- This is an unsupervised machine learning task called Clustering.
{% endif %} 


