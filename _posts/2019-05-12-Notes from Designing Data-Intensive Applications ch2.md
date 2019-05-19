---
layout: post
last_update_date: May 12, 2019
book_notes: true
title: Designing Data-Intensive Applications part 2
brief: >-
  This post collects some notes, definitions or quotes from ch2 of Martin Kleppmann's book
  Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems
---

<h3 class="post-sub-title center">Ch 2: Data Models and Query Language</h3>

<div class="post-table center">
  <h4>Document vs Relational Databases</h4>
  <table>
    <thead>
      <tr>
        <th></th>
        <th>Document Database (NoSQL)</th>
        <th style="width: 200px">Relational Database</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="centered-td">Pros</td>
        <td>
          <ul>
            <li>schema Flexibility</li>
            <li>better performance due to locality</li>
            <li>storing data in a closer structure as the one used in the applications</li>
          </ul>
        </td>

        <td>
          <ul>
          <li>many to many</li>
          <li>many to one</li>
          <li>joins</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</div>

<div class="def">
  <h3>Locality</h3>
  <p>means loading all data at once.</p>
</div>

<div class="def">
  <h3>The query optimizer</h3>
  <p>in Relational database automate the selection of the "access path" to the data by choosing the best indexes/paths to access the data.</p>
</div>

<div class="def">
  <h3>MapReduce:</h3>
  <p>using some imperative code/methods to be applied in parallel while getting the data using declarative language <i>(online definition: a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster)</i></p>

<br>

<h5>For example:</h5>

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

<br>
<p>There are other data models, like Network Model (e.g. CODASYL) and Graph-Like data model.</p>

<br><br><br>
<h2 class="center">to be continued</h2>
