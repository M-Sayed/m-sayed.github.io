---
layout: post
last_update_date: May 12, 2019
book_notes: true
title: Summary of Chapter 2 of Designing Data-Intensive Applications
brief: >-
  This post collects some notes, definitions or quotes from ch2 of Martin Kleppmann's book
  Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems
---

### Document vs Relational Databases

<br>

 Content     | Document Database (NoSQL) | Relational Database
------------ | ------------------------- | -------------------
Pros         | Schema Flexibility, better performance due to locality and storing data in a closer structure as the one used in the applications      | Many to many, many to one and joins

<br>

### Locality:

means loading all data at once.

### The query optimizer

in Relational database automate the selection of the "access path" to the data by choosing the best indexes/paths to access the data.

### MapReduce:

using some imperative code/methods to be applied in parallel while getting the data using declarative language _(online definition: a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster)_


##### For example:

{% highlight js %}
      db.observations.mapReduce(
           function map() {
                   var year = this.observationTimestamp.getFullYear();
                   var month = this.observationTimestamp.getMonth() + 1;
                   emit(year + "-" + month, this.numAnimals);
           }, function reduce(key, values) {
                   return Array.sum(values);
           }, {
                   query: { family: "Sharks" },
                   out: "monthlySharkReport"
           }
      );
{% endhighlight %}
</div>


There are other data models, like Network Model (e.g. CODASYL) and Graph-Like data model.
