---
title: How I Prepared for AWS ML Specialty Certification
layout: single
date: '2021-08-02 10:19:25 +0530'
toc: true
tags:
- aws
- certification
- machinelearning
---

**My Objective and Preparation Strategy to clear this Specialty Exam**

![]({{ '/assets/images/aws-certified-machine-learning-specialty.png' | relative_url }})

# Introduction
Last week I had cleared AWS Certified Machine Learning Specialty Exam and after that, I am getting a lot of questions about exams and how did I prepare for this exam. In this post, I am sharing my objective of taking this exam, preparation strategy, and resources I have referred. I hope it will be helpful to someone who is planning to take this certification.

# Objective for taking the exam
I am working in the Machine Learning domain for almost two years and most of my learning came either from online courses or Pet Projects/POCs(Proof Of Concepts), which is not a structured way of learning so as a result I was left with many weak concepts and understanding gap. The curriculum for this certification brings **Structure Learning** as it covers the whole Machine Learning Cycle along with AWS-specific services.

Another reason behind taking this exam is to gain knowledge for building and deploying **End to End Machine Learning Products in Cloud.** The majority of my work is POCs and Pet projects which most of the time ends up in Juypter notebook in GIT and never deployed to Production, this preparation helps me to bridge the gap of building reliable and effective machine learning architecture in the cloud.

>**Tip**: If you want to focus more on the ML domain then start your preparation with that and then move to AWS specific content, this will help you to build confidence in the domain

# About the Exam
As this is a Specialist exam and emphasis a lot on the domain, this is different from other AWS certifications and needs proper planning and time allocation. The exam is split into 4 domains: Data Engineering (20%), Exploratory Data Analysis(EDA) (24%), Modelling (36%), and ML Implementation & Operations (20%). The content within EDA and Modelling is a balance of domain and specific AWS services, whereas the Data Engineering is more on the AWS side. For MLOps, I have found that the majority of the content got covered in the Modelling section. They are expecting real-time experience in the Machine learning field so make sure that you have some working experience in the field.

>**Tip** : I have booked the exam date in advance before starting my preparation, this helped me to have time-bound and focused preparation. You will have two chances to postpone the exam, but try to avoid rescheduling

# Preparation Strategy and Resources
I have put in close to **185** hours in the span of **4** months to prepare for this exam, referred following online material in the same order

* AWS Resources — I have started from [Machine Learning Path](https://aws.amazon.com/training/learning-paths/machine-learning/data-scientist/) that AWS suggests taking to prepare for the exam. From this path, I have picked only [The Elements of Data Science](https://www.aws.training/Details/eLearning?id=26598), and the [Exam Readiness](https://www.aws.training/Details/eLearning?id=42183) course. The first one is a very basic and refresher course and the second one talks about the content that is expected to know in each of the domains and their sub-domains, use this as a reference to check your readiness for the exam
* Udemy — [AWS Certified Machine Learning Specialty 2021 — Hands On!](https://www.udemy.com/course/aws-machine-learning/) By Stephane Maarek and Frank Kane. This is a deep dive course and gives you the full picture of exam content
* Sage Maker — [AWS Official Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) and [Amazon SageMaker Technical Deep Dive Series](https://www.youtube.com/watch?v=uQc8Itd4UTs&list=PLhr1KZpdzukcOr_6j_zmSrvYnLUtgqsZz) . Amazon SageMaker is a fully managed machine learning service and very much important in terms of exam content, Modelling and ML Ops sections are heavily dependent on this service. It’s a common piece of advice from another exam taker to read plenty of SageMaker official documentation, but I found this one is a little intimating as it is very lengthy. To understand the service thoroughly I have referred to deep-dive videos which are series of 16 videos and I found them very useful.

Along with the above content, I have referred to some generic available articles/blog posts to understand the concept and prepared notes in this [Trello board](https://trello.com/b/Sx6lJzy8). These notes are distributed in four Lists, each list represents one domain of the exam. Each note is labelled with priority along with resources links, screenshots. This board becomes a Kanban board which helped me to stay on top of my learning.

![]({{ '/assets/images/trello_board-snapshot.png' | relative_url }})
													*Trello Board Snapshot*

![]({{ '/assets/images/trello_sample_card.png' | relative_url }})
																		*Sample Card from Trello board*

>**Tip**: As there is so much to learn, it is easy to get overwhelmed and lose track of what you have already learned and what needs to be covered next. In this case, your notes will come to the rescue. I will recommend preparing notes for this exam, it will also help you in last-minute revision

# Practice Exam
In last week of my preparation I have given around 10 Practice set which helped me to understand my weak topics and where I need to focus more. I have put links along with recommendation for all these mock/practice test in ‘Resource’ list of [Trello board](https://trello.com/b/Sx6lJzy8) .

# Real Exam
I was a little skeptical before the actual exam date as I have not secured a great score in most of the practice exams and I am lacking in confidence. Since I had committed to myself not to change the exam date, so I went for it and passed the exam with 86.5%. During the exam, I have used the Process of Elimination extensively to remove wrong choices and I guess that worked for me because in the mock exam I was not using this technique.

>**Tip**: Take your mock/practice exam seriously as it will help you to build your confidence for the real exam. Try to give mock exams in real-time exam like time-bound manner

# Other resources
Apart from above-mentioned resources, I have referred following blogs which helped me to get started and sources to useful materials

* [Blog](https://towardsdatascience.com/how-i-prepared-for-the-aws-machine-learning-speciality-certification-10834924d192) by Raghav Dave
* Similar [blog post](https://simpledataflow.com/machine-learning-specialty-exam/) by Simple Data flow
* I have also referred book [Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.amazon.co.uk/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646) to understand some core concepts

# Last word !!
Along with lengthy and difficult certification to achieve this one is expensive also, so be clear in your objective —**why you want to take this exam**. As mentioned, my objective was to have structured learning to fill the gap in my knowledge and understanding to build reliable and effective machine learning architecture in the cloud, make sure you have your valid reason and objective before committing for this specialist certification.
