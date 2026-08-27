# 📰 Daily News Bot - 48+ Commits Daily

**Last Update:** 2026-08-27 19:43:55

**Total News:** 12

**Sources:** Al Jazeera, Hacker News, NASA, BBC

---

## 📰 Latest News

### 1. Japanese polka dot artist Yayoi Kusama dies aged 97

**Source:** Hacker News

**Category:** technology

**Description:**
<p>Article URL: <a href="https://www.bbc.com/news/articles/c3v4k0re3vwo">https://www.bbc.com/news/articles/c3v4k0re3vwo</a></p>
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=49466865">https://news.ycombinator.com/item?id=49466865</a></p>
<p>Points: 22</p>
<p># Comments: 1</p>

🔗 **Read more:** [https://www.bbc.com/news/articles/c3v4k0re3vwo](https://www.bbc.com/news/articles/c3v4k0re3vwo)

---

### 2. Launch HN: Salem Robotics (YC S26) – Software for industrial inspection robots

**Source:** Hacker News

**Category:** technology

**Description:**
<p>Hi HN, we're the founders of Salem Robotics (<a href="https://salemroboticsinc.com">https://salemroboticsinc.com</a>). We give existing mobile robots the task-specific intelligence to carry out surveys and physically interactive inspections in hazardous industrial facilities.<p>Here's a video of it running on real robot hardware with a few words from us:
<a href="https://youtu.be/U_228h3NE7c" rel="nofollow">https://youtu.be/U_228h3NE7c</a><p>We came to Salem through robotics research at UT Austin and a combined 15 years working in nuclear, including about 10 years developing and deploying autonomous robots at Los Alamos National Laboratory. Over the last five years, we kept running into the same gap: robot hardware had become very capable, but making a robot carry out a complete industrial procedure still required a surprising amount of robotics work and manual intervention.<p>The part that interested us most was manipulation. A nuclear contamination survey, for example, can require taking a "smear": wiping a defined area of a surface so it can be checked for removable radioactive contamination. In an oil, gas, or chemical facility, an LDAR (leak detection and repair) inspection can require moving a detector around a particular valve, flange, or connection. Other inspections require positioning an instrument at a precise location and orientation relative to a pipe or piece of equipment.<p>These are easy tasks to compress into verbs like "wipe", "measure", or "inspect", but considerably harder to make a robot do reliably. A probe might need to remain normal to a surface throughout a path, stay within a narrow offset from a pipe, or trace a region while maintaining a particular end-effector orientation. The planner has to find a feasible motion while respecting the task geometry, manipulator kinematics, joint limits, collisions, and the environment around it.<p>We work down to joint-level control for those interactions. One problem we've spent a lot of time on is generating constrained manipulation plans quickly enough that they can be based on the geometry the robot actually observes instead of requiring someone to carefully author a trajectory for every individual surface, valve, or flange.<p>The physical world makes this annoying. A few centimeters of error may not matter much when navigating down a hallway, but it matters if a sensor is supposed to remain normal to a curved surface. And successfully executing a trajectory doesn't necessarily mean the inspection worked. The detector could be misaligned, contact could be wrong, the geometry could differ from the model, or the measurement itself could be invalid. We care about closing that loop around the inspection result, not just whether the arm reached the commanded pose.<p>Our approach is a combination of AI and classical robotics. A lot of robotics research and industry attention right now is going toward increasingly end-to-end learned systems, particularly around humanoids. Working in safety-critical environments has made us appreciate how relevant classical approaches still are when you want explicit constraints, predictable behavior, and theoretical guarantees about what a robot can and cannot do.<p>We use AI where semantic understanding and flexibility are useful, such as interpreting less structured information or understanding what in an unfamiliar scene is relevant to a procedure. Once the system knows what physical interaction it needs to perform, we prefer explicit geometry, planning, optimization, and control where possible. We're interested in the marriage between the two rather than trying to make every part of the robotics stack learned.<p>The other idea behind Salem is that we don't think every useful robot application should require building a new robot. Companies like Boston Dynamics are getting very good at building increasingly capable hardware platforms. We think there is room for a domain-specific application layer on top of that hardware. The same underlying robot might perform nuclear radiological surveys in one facility and LDAR inspections in another, but the procedures, sensors, manipulation constraints, success conditions, and outputs are different.<p>That's also why we're hardware agnostic. We don't expect one robot to be the best platform forever, and facilities already own different hardware. We'd rather describe an inspection in terms of what needs to happen and then map that onto the capabilities of the right robot for the job.<p>One thing that surprised us after spending more time with facilities is how manual many inspection workflows still are. In sophisticated nuclear and industrial sites, people still physically walk survey routes, take measurements one at a time, visually inspect equipment, record results manually, and sometimes make judgments based on things like how a component sounds. Some of the basic workflows would be recognizable to someone doing the job decades ago, even though the sensors, computation, and robots available today are radically different.<p>We're starting with radiological inspection in nuclear because it's the industry we know best, and we're also working on manipulation-heavy inspection problems in oil, gas, and hazardous chemical facilities. The technicians and inspectors still define the procedure, interpret results, and make the consequential judgments. We're trying to automate more of the repetitive physical execution that currently requires someone to enter the environment or manually operate a robot.<p>We sell directly to industrial facilities, usually starting with a paid technical validation and then moving to an ongoing deployment. Pricing varies substantially with the workflow: validations range from tens of thousands to over $100k, and larger deployments can range from the low hundreds of thousands to roughly $500k per robot.<p>One thing we're especially curious to hear HN's thoughts on is where the abstraction boundary in robotics should sit. What should come from the robot manufacturer, what belongs in an application layer, and what will inevitably remain specific to the facility? We'd also be interested in hearing about other industries where you've seen physical inspection tasks that look trivial to a person but are surprisingly difficult to automate.</p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=49466715">https://news.ycombinator.com/item?id=49466715</a></p>
<p>Points: 5</p>
<p># Comments: 1</p>

🔗 **Read more:** [https://news.ycombinator.com/item?id=49466715](https://news.ycombinator.com/item?id=49466715)

---

### 3. Corporate political donations shatter record at $646M so far for US midterms

**Source:** Hacker News

**Category:** technology

**Description:**
<p>Article URL: <a href="https://www.reuters.com/legal/government/corporate-political-donations-shatter-record-646-million-so-far-us-midterms-2026-08-27/">https://www.reuters.com/legal/government/corporate-political-donations-shatter-record-646-million-so-far-us-midterms-2026-08-27/</a></p>
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=49466220">https://news.ycombinator.com/item?id=49466220</a></p>
<p>Points: 16</p>
<p># Comments: 2</p>

🔗 **Read more:** [https://www.reuters.com/legal/government/corporate-political-donations-shatter-record-646-million-so-far-us-midterms-2026-08-27/](https://www.reuters.com/legal/government/corporate-political-donations-shatter-record-646-million-so-far-us-midterms-2026-08-27/)

---

### 4. Watch: How the collapse of a glacier caused such devastation

**Source:** BBC

**Category:** world

**Description:**
At least 270 people have died in the massive flash floods, while more than 800 others are missing.

🔗 **Read more:** [https://www.bbc.co.uk/news/videos/ckgxnrg8j19o?at_medium=RSS&at_campaign=rss](https://www.bbc.co.uk/news/videos/ckgxnrg8j19o?at_medium=RSS&at_campaign=rss)

---

### 5. Uefa preparing criminal legal action against Infantino

**Source:** BBC

**Category:** world

**Description:**
Uefa is pursuing criminal proceedings against Fifa president Gianni Infantino over the scrapped plan to sell off stakes in the World Cup.

🔗 **Read more:** [https://www.bbc.co.uk/sport/football/articles/cx2zl5kwlxjo?at_medium=RSS&at_campaign=rss](https://www.bbc.co.uk/sport/football/articles/cx2zl5kwlxjo?at_medium=RSS&at_campaign=rss)

---

### 6. Convicted Bosnian Serb war criminal Mladić dies aged 84

**Source:** BBC

**Category:** world

**Description:**
He was jailed for life in 2017 for genocide, war crimes and crimes against  humanity during the wars in the ex-Yugoslavia in 1992-95.

🔗 **Read more:** [https://www.bbc.co.uk/news/articles/c5ywxpryj95o?at_medium=RSS&at_campaign=rss](https://www.bbc.co.uk/news/articles/c5ywxpryj95o?at_medium=RSS&at_campaign=rss)

---

### 7. UEFA asks US court for FIFA documents for criminal case against Infantino

**Source:** Al Jazeera

**Category:** world

**Description:**
European football&#039;s governing body considering ‌criminal complaint ​against Infantino over World Cup selloff plans.

🔗 **Read more:** [https://www.aljazeera.com/sports/2026/8/27/uefa-asks-us-court-for-fifa-documents-for-criminal-case-against-infantino?traffic_source=rss](https://www.aljazeera.com/sports/2026/8/27/uefa-asks-us-court-for-fifa-documents-for-criminal-case-against-infantino?traffic_source=rss)

---

### 8. Burnham’s expected UK ban on Israeli settlement goods draws broad support

**Source:** Al Jazeera

**Category:** world

**Description:**
A Labour lawmaker tells Al Jazeera sanctions would uphold British morals and legal obligations.

🔗 **Read more:** [https://www.aljazeera.com/news/2026/8/27/do-more-than-just-condemn?traffic_source=rss](https://www.aljazeera.com/news/2026/8/27/do-more-than-just-condemn?traffic_source=rss)

---

### 9. Tottenham sign Man City’s Egypt forward Omar Marmoush on season-long loan

**Source:** Al Jazeera

**Category:** world

**Description:**
Deal includes an obligation to make the move permanent next year, reportedly for a ⁠guaranteed $68m.

🔗 **Read more:** [https://www.aljazeera.com/sports/2026/8/27/tottenham-sign-man-citys-egypt-forward-omar-marmoush-on-season-long-loan?traffic_source=rss](https://www.aljazeera.com/sports/2026/8/27/tottenham-sign-man-citys-egypt-forward-omar-marmoush-on-season-long-loan?traffic_source=rss)

---

### 10. Tropical Storm Julio

**Source:** NASA

**Category:** nature

**Description:**
Natural event: Severe Storms

🔗 **Read more:** [https://eonet.gsfc.nasa.gov/api/v3/events/EONET_23286](https://eonet.gsfc.nasa.gov/api/v3/events/EONET_23286)

---

### 11. Wildfire Old Deer, Carson, Texas

**Source:** NASA

**Category:** nature

**Description:**
Natural event: Wildfires

🔗 **Read more:** [https://eonet.gsfc.nasa.gov/api/v3/events/EONET_23209](https://eonet.gsfc.nasa.gov/api/v3/events/EONET_23209)

---

### 12. Wildfire 22, Miami-Dade, Florida

**Source:** NASA

**Category:** nature

**Description:**
Natural event: Wildfires

🔗 **Read more:** [https://eonet.gsfc.nasa.gov/api/v3/events/EONET_23225](https://eonet.gsfc.nasa.gov/api/v3/events/EONET_23225)

---


**Built with ❤️ by GitHub Actions**