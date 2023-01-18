{# templates/markdown.txt #}

<h1 align="center"> {{title}} </h1>

<h3 align="center"> {{subtitle}} </h3>

<h5 align="center"> {{description}} </h5>




## Overview:

<table cellspacing="1" cellpadding="2" valign="middle" style="border-collapse: collapse; border: none;">
  <tbody>
    <tr style="border: none;">
      <td style="border: none;">
      <h3 > Training Data </h3>

- {% if x_train_0 is defined %} **{{ x_train_0 }}** observations {% else %} 0 observations {% endif %} and **{{ x_train_1 }}** features
  
  {% if regression %}
- The target variable **{{ y_train_name}}** is **{{ type_y_train }}** with mean **{{ mean_y_train}}** and standard deviation **{{ std_y_train}}**. 
  {% else if classification%}
    {% if imbalanced %}
- This is a case of imbalanced classification where the data set has the following skewed proportions{{ class_1_name }}: {{ class_1_count}} ({{class_1_prop}}%) and {{ class_2_name }}: {{ class_2_count}} ({{class_2_prop}}%).
    {% endif %}

  {% else %}
- This is an unsupervised machine learning task called Clustering.
  {% endif %} 
        </td>
      {%if picture}
      <td style="border: none;">
        ![](assets/HackerRank-Dashboard.png)
      </td>
  </tbody>
</table>
