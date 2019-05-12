---
layout: post
last_update_date: May 12, 2019
book_notes: true
---

# Notes from Designing Data-Intensive Applications

## Chapter 2: Data Models and Query Language

### Document vs Relational Databases:

<style>
  ul{ list-style-type: none; padding-left: 10px; margin: 0; }
  th { text-align: center }
  .centered-td { text-align:center }
  table, th, td { border: 1px solid black; }
  td { min-width: 50px; }
</style>

<table style="border: 1px solid black;">
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

**Locality:** means loading all data at once.
**The query optimizer** in Relational database automate the selection of the "access path" to the data by choosing the best indexes/paths to access the data.

There are other data models, like Network Model (e.g. CODASYL) and Graph-Like data model.

#### **MapReduce:**
using some imperative code/methods to be applied in parallel while getting the data using declarative language _(online definition: a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster)_

**For example:**
```js
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
```
