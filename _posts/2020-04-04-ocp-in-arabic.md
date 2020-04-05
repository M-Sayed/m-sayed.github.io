---
layout: post
lang: ar
img_name: ocp-in-arabic-img-1.jpg
last_update_date: Apr 5, 2020
book_notes: false
title: Open-closed principle
categories: [ar]
brief: >-
  The `O` in SOLID. What is Open-Closed Princible?
---

<div dir="rtl">
الـ open-closed principle بيقول إن لو عندنا class، فالكلاس ده يكون غير قابل للتعديل ولكن قابل للتمدد، بمعني إن الكلاس يكون قادر إنه يهندل لوجيك أكتر من غير ما أعدل الكود بتاع الكلاس نفسه.

حاجة زي دي ممكن تتنفذ بعدة طرق، أوضحهم هي الـ dependency injection وده معناه إن لو الكلاس بينفذ لوجيك معين ممكن يتغير بتغير الـ objects اللي بتنفذ اللوجيك ده، فالـ objects دي يستحسن يتعملها depencey injection للكلاس، خلونا نأخد مثال:

<div dir="ltr">
<script src="https://gist.github.com/M-Sayed/66ba9b543f24ace41ad385bc6e39a601.js"></script>
</div>

واضح في المثال اللي فات ده إن اللوجيك اللي بيتنفذ بيعتمد علي الـ object اللي إسمه Paypal، فاللي هيحصل في حالة إننا حبينا نغير ال payment gateway دي لحاجة تانية زي Strip هنضطر إن أحنا نعدل الكلاس Order ونغير من Paypal لـ Strip، تغير الكود ده هو اللي المفروض نتجنبه ولكن في نفس الوقت محتاجين من غير ما نغير الكود إن أحنا نخلي ال Order كلاس يدعم payment gateways أكتر، فحاجة زي دي ممكن تتحق بالـ dependency injection/inversion واللي هو أصلا واحد من مبادئ الـ SOLID، فالكود هيكون بالمنظر ده.

<div dir="ltr">
<script src="https://gist.github.com/M-Sayed/1a322a42ee91d6df1843b4a94bcd5d24.js"></script>
</div>

هل فيه طرق تانية نقدر نحقق بيها مبدأ ال OCP؟ فيه طبعاً وده اللي هنكمله في الجزء التاني من البوست ده.
</div>
