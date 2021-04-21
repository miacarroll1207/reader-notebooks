

Distant Reader Notebooks
========================

This repository includes a set of Jupyter Notebooks and sample data intended to instruct students, researchers, and scholars on the application of text mining & natural language processing against Distant Reader outputs -- affectionately known as "study carrels". People who go through these notebooks will learn how to:

  1. apply text mining & natural language processing against one or more plain text files (such as the whole of *Moby Dick* or hundreds of journal articles on the topic of COVID-19), and/or
  2. take fuller advantage the thing called the [Distant Reader](https://distantreader.org)


Table of contents
-----------------

These notebooks are divided into the following sections:

   1.  [What is the Distant Reader, and why should I care?](./README.md)
   2.  [Getting started](./notebooks/02-getting-started.ipynb)
   3.  [Rudimentary analysis](./notebooks/02-rudimentary.ipynb)
   4.  [Frequencies](./notebooks/03-frequencies.ipynb)
   5.  [Parts-Of-Speech](.notebooks/04-parts-of-speech.ipynb)
   6.  [Word clouds](./notebooks/05-word-clouds.ipynb)
   7.  [Feature Extraction with Textacy](./notebooks/06-feature-extraction-with-textacy.ipynb)
   8.  [SQL](./notebooks/07-sql.ipynb)
   9.  [Catalog; The "Public" Library](./notebooks/08-catalog.ipynb)
   10. [Harvest](./notebooks/09-harvest.ipynb)
   11. [Topic Modeling](./notebooks/10-modeling.ipynb)


What is the Distant Reader, and why should I care?
--------------------------------------------------

The Distant Reader is a tool for reading.

With the advent of the Internet people feel as if they are "drinking from a firehose" -- ofttimes called "information overload". The Distant Reader is a tool enabling students, researchers, or scholars to embrace information overload, identify patterns & trends in the things they read, and ultimately use & understand their readings more thoroughly. In this way, the Distant Reader is not a replacement for traditional reading. Instead, the Distant Reader is intended to supplement the traditional reading process.

The Distant Reader is a Web-based service freely available to anybody with a Web browser and an Internet connection. The Distant Reader is located at [https://distantreader.org](https://distantreader.org), but these notebooks are not about the Distant Reader, *per se*; these notebooks are about text mining, natural language processing, and things called Distant Reader "study carrels". 


What are text mining & natural language processing?
---------------------------------------------------

Text mining & natural language processing represent complementary methods used to derive information (and hopefully knowledge) from the data contained in one more more narrative texts.

Text mining is akin to "descriptive statistics" applied against one or more documents; it enumerates & illustrates the data found in a narrative. It highlights the "features" of texts. For example, given a text (like *Moby Dick*) it is relatively easy to count & tabulate the number of times the word "whale" occurs. It is just as easy to count & tabulate the occurrences of "white whale". Similarly, it is easy to count the frequency of the word "Ahab" as well as its proximity to the phrase "white whale". In fact, because of this proximity, we might even posit there is some sort of relationship between "white whale" and "Ahab". Given all the tokens (numbers, words, etc.) in a text, as well as their ordinal locations (first token, second token, etc.), it is possible to answer rudimentary questions like but not limited to:

   * How big is this document?
   * How big is this document compared to other documents?
   * What words are in this document?
   * How many times do those words occur?
   * Is a given word in this document; what words don't appear in this document?
   * What two-word phrases exist and how often?
   * How repetitive is the language of the document; how difficult is a document to comprehend?
   * What words or phrases can be considered statistically significant?

Furthermore, it is entirely possible to illustrate the answers to these question using any number of standard visualizations (bar charts, pie charts, histograms, word clouds, etc.). Text mining exposes the data in a text, the data is turned into information because "white whale" means something to you, and if there are patterns or anomalies illustrated in the charts & graphs, then we might say some sort of knowledge has been obtained. 

Natural language processing is more akin to "inferential statistics". It picks up where text mining leaves off. Natural language processing is a two-step technique. The first step is to identify patterns found in many texts. For example, "A list of words where the first word is capitalized, and the last word is followed by a punctuation mark can probably be called a 'sentence'", or "In English, words ending in 'ed' are often past tense verbs", or "The word following 'Mr.' is more often than not the name of male person." These patterns are manifested in one of two ways:

   1. through the combination of symbols (such as DET-ADJ-ADJ-NOUN denoting "determiner adjective adjective noun", and "the quick brown fox" matches this pattern), or
   
   2. a set of vectors denoting the characteristics of words when compared to other words and other documents, and these sets of vectors are often called "models"

The second step of natural language processing is to identify words or sets of words which match one or more of the patterns. By doing so the words can be given contexts in the form of parts-of-speech, named entities, and/or grammars such as noun phrases, prepositional phrases, quotations, or even sentences in the form of subject-verb-object. Once natural language processing is done the student, researcher, or scholar can address complex questions. Some of those questions are classic newspaper reporter-like questions, such as: who, what, when, where, how, and how many. ("Why" is a very difficult question to answer.) The questions can also be sublime: "What is this person's definition of 'love', and how does it compare to that person's definition"; "When is war justified", or; "What does it mean to be a 'good human being'?"

More figuratively stated, text mining & natural language processing are complementary methods for "climbing the Ladder of Understanding". This metaphorical Ladder has four rungs. The lowest and most fundamental rung is "data" where data is represented as numbers, words, or a combination of the two. Examples include "1776" and "chestnut". The second rung of the Ladder is "information", which is defined as data put into context. For example, "1776 is a year." The third rung of the Ladder is "knowledge" -- information which is useful & understood. For example, "In the year 1776 the Constitution of the United States was written, and the Constitution outlined a form of government which had not previously been articulated." The fourth and final rung of the Ladder is "wisdom" -- knowledge of a timeless nature. (Examples of wisdom are for a different essay.) Through the use of text mining & natural language processing, a person can extract data from a text, turn the data into information, and posit whether or not it represents knowledge.

The Distant Reader applies both text mining & natural language processing against texts. The result of the Distant Reader process is data set primed for analysis ("reading"). These data sets are called "study carrels".


What are "study carrels"?
-------------------------

Study carrels are the names given to Distant Reader outputs; they are structured data sets lending themselves to analysis ("reading") by people or computers. 

Given an almost arbitrary amount of unstructured data (think "text"), the Distant Reader outputs sets of structured data -- study carrels. Each study carrel is made of exactly the same set of parts:

   1. a cache of the originally submitted files
   2. a set of plain text files transformed from the cache
   3. a file which makes up the whole of Item #2
   4. a rudimentary narrative report summarizing the carrel
   5. a set of interactive reports summarizing the carrel
   6. a set of bibliographics
   7. a set of ngrams
   8. a set of statistically significant keywords
   9. a set of words, their locations, their lemmas, and their parts-of-speech
  10. a set of named entities, their locations, and their types
  11. a set of URLs
  12. a set of email addresses
  13. a set of rudimentary grammars
  14. a set of charts & graphs illustrating Items #7-10.
  15. a database file containing Items #6-12

There are three very important characteristics of each & every study carrel. First, each study carrel is computer platform independent, meaning, any computer ought to be able to read every file a study carrel contains; none of the files (with the exception of the database file) require specialized software. Second, study carrels are network independent, meaning, a person does not need the Internet in order to use a study carrel; you could be in a concrete bunker deep inside a mountain with your computer and a study carrel, and the study carrel would still be operational. Thirdly, and as already mentioned many times, study carrels are sets of structured data, meaning: 1) every file is in the same location from carrel to carrel to carrel, and 2) the files they contain lend themselves to computing *very easily*.

Study carrels are manifestations of the data & information extracted from one or more texts. The purpose of these notebooks is to outline & demonstrate how to computationally analyze ("read") this data & information and ultimately garner knowledge -- information which is useful & understood.


How to use these notebooks
--------------------------


--- 
Eric Lease Morgan &lt;<a href="mailto:emorgan@nd.edu">emorgan@nd.edu</a>&gt;  
April 21, 2021

