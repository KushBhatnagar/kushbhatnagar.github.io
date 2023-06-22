---
permalink: /mlops-playground/
layout : category
title: "The MLOps Playground"
---

In this series, I dive into the landscape of MLOps tools that enable seamless integration, testing, and deployment of ML models. In addition, I explore the numerous benefits offered by various AWS cloud services specifically designed for Machine Learning lifecycles. Throughout this series, I will also delve into the complexities of designing effective model deployment architectures, while venturing into the realms of continuous delivery and automated machine learning pipelines


{% for post in site.categories.mlops %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}

