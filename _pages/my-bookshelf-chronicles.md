---
permalink: /my-bookshelf-chronicles/
layout : category
title: "My bookshelf Chronicles!!"
---

In this series, I'll be sharing my personal reflections on the books that have resonated with me, books that have left a lasting impression, sparked new insights or simply offered a moment of respite from the daily grind. My reading list is eclectic and random, but each book has something to offer


{% for post in site.categories.bookshelf %}
 <li><span>{{ post.date | date_to_string }}</span> &nbsp; <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}

