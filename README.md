# 📰 Daily News Bot - 48+ Commits Daily

**Last Update:** 2026-10-12 21:02:04

**Total News:** 12

**Sources:** NASA, Al Jazeera, BBC, Hacker News

---

## 📰 Latest News

### 1. Muse Wonder

**Source:** Hacker News

**Category:** technology

**Description:**
<p>Article URL: <a href="https://research.meta.ai/blog/muse-wonder">https://research.meta.ai/blog/muse-wonder</a></p>
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=50059115">https://news.ycombinator.com/item?id=50059115</a></p>
<p>Points: 58</p>
<p># Comments: 17</p>

🔗 **Read more:** [https://research.meta.ai/blog/muse-wonder](https://research.meta.ai/blog/muse-wonder)

---

### 2. Launch HN: Agent37 (YC F26) – Low-cost agent sandboxes for running agents

**Source:** Hacker News

**Category:** technology

**Description:**
<p>Hey HN, I’m Vishnu from Agent37 (<a href="https://agent37.com">https://agent37.com</a>). We build sandboxes for running AI agents at under 10% of the cost of most sandbox providers. Our customers spend an average of $0.37/month per sandbox.<p>You can view a video walkthrough of the product here: <a href="https://youtu.be/DK5ISR2tbNo" rel="nofollow">https://youtu.be/DK5ISR2tbNo</a><p>We started as one of those OpenClaw wrapper companies back in February (yup.. judge me). In time we added more and more harnesses.<p>One of the goals I had at the time was to offer a free plan to users, so as to gain more market share. But it was too cost prohibitive to do it right away. Especially since we were bootstrapped and servers were running on my savings.<p>Today we’re actually able to offer the free plan thanks to the optimizations we’ve made since. Over 90% of the new signups we have are just free plan users and they host their personal Hermes/Openclaw/Claude Code etc on our cloud. Our infrastructure cost for the free sandboxes averages around $0.05 to $0.10 per user per month.<p>Here are some techniques that have worked for lowering cost:<p>* When you look at agent harnesses, they have certain patterns in the way they consume CPU and RAM. They need CPU in bursts when they’re initializing or performing certain tasks, but beyond that, they’re often not peaking. They need more RAM for things like browser and computer-use tasks. Once the task is done, usage often comes back down. This is a key insight in lowering cost, so by efficiently managing the CPU/RAM utilization we could lower the cost.<p>* Secondly, you have to skip the hyperscalers when renting the Hosts. I worked at Amazon before and they have 80-90% margins on VMs. So it was an obvious choice once I looked at the prices to go one layer down to vendors like Hetzner and OVH. This alone was probably one of the biggest cost levers in reducing the cost.<p>* Thirdly, you also want to pick a technology stack that lets you efficiently cache and share resources across the host. We use gVisor for better utilization and fast boot times. It lets us use available host memory across sandboxes without reserving a full VM’s memory for each one. There are tradeoffs: our gVisor sandboxes don’t support workloads like Docker-in-Docker or Android emulators.<p>* And finally the size and shape of the hosts you buy also makes a big difference. RAM is typically the bottleneck when it comes to cost and not the CPU. This is specifically true for agent harness workloads, so when buying servers, we optimize for packing more RAM into a given host.<p>We also host full VM sandboxes for workloads that need them, including running Docker at a slightly higher price, but they are still pretty low cost given the rest of the techniques.<p>Overall, my learning has been that just by focusing on a niche of sandbox usecases, and optimizing for it you can give a much better cost/performance tradeoff.<p>I was previously a Senior Software Engineer at Amazon and an Engineering Manager at Quantcast. I built Amazon's internal AI chatbot, Diya, and their internal coding harness, Ziya.<p>If you’re someone who’s looking to run agents on sandbox and are exploring a sandbox vendor, come check us out. We’re particularly looking for developers building messaging agents to try their workloads and challenge the limits and economics of our platform.<p>Thanks!<p><a href="https://agent37.com">https://agent37.com</a></p>
<hr />
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=50059096">https://news.ycombinator.com/item?id=50059096</a></p>
<p>Points: 5</p>
<p># Comments: 0</p>

🔗 **Read more:** [https://news.ycombinator.com/item?id=50059096](https://news.ycombinator.com/item?id=50059096)

---

### 3. Reverse engineer anything with agents, from app behavior down to native binaries

**Source:** Hacker News

**Category:** technology

**Description:**
<p>Article URL: <a href="https://github.com/morluto/rea">https://github.com/morluto/rea</a></p>
<p>Comments URL: <a href="https://news.ycombinator.com/item?id=50058850">https://news.ycombinator.com/item?id=50058850</a></p>
<p>Points: 5</p>
<p># Comments: 0</p>

🔗 **Read more:** [https://github.com/morluto/rea](https://github.com/morluto/rea)

---

### 4. Britain won't tolerate threats on our soil, Miliband says as he summons Iran ambassador

**Source:** BBC

**Category:** world

**Description:**
The prime minister says Iran's Islamic Revolutionary Guard "almost certainly" directed the RAF Fairford incident.

🔗 **Read more:** [https://www.bbc.co.uk/news/articles/c6gr82ekqewyo?at_medium=RSS&at_campaign=rss](https://www.bbc.co.uk/news/articles/c6gr82ekqewyo?at_medium=RSS&at_campaign=rss)

---

### 5. Six Ukrainian energy sites hit by Russia since Trump announced ceasefire, Zelensky says

**Source:** BBC

**Category:** world

**Description:**
Despite the US president announcing energy infrastructure would not be targeted strikes have continued, Ukraine says.

🔗 **Read more:** [https://www.bbc.co.uk/news/articles/cvlyd4pdlwkxo?at_medium=RSS&at_campaign=rss](https://www.bbc.co.uk/news/articles/cvlyd4pdlwkxo?at_medium=RSS&at_campaign=rss)

---

### 6. Watch: What could Trump's energy ceasefire mean for Ukraine?

**Source:** BBC

**Category:** world

**Description:**
The BBC's Dan Johnson reports from Kyiv, where Ukrainians face another winter with electricity outages.

🔗 **Read more:** [https://www.bbc.co.uk/news/videos/crd9321ygqw8o?at_medium=RSS&at_campaign=rss](https://www.bbc.co.uk/news/videos/crd9321ygqw8o?at_medium=RSS&at_campaign=rss)

---

### 7. ‘Totally unfair’: Navi Pillay slams US sanctions against ICC

**Source:** Al Jazeera

**Category:** world

**Description:**
Nobel Peace Prize winner Navi Pillay has condemned US sanctions against the International Criminal Court.

🔗 **Read more:** [https://www.aljazeera.com/video/newsfeed/2026/10/12/totally-unfair-navi-pillay-slams-us-sanctions-against-icc?traffic_source=rss](https://www.aljazeera.com/video/newsfeed/2026/10/12/totally-unfair-navi-pillay-slams-us-sanctions-against-icc?traffic_source=rss)

---

### 8. Blast kills teenager, injures dozens in northern Israel

**Source:** Al Jazeera

**Category:** world

**Description:**
A 15-year-old was killed and around 20 people injured when unexploded ordnance detonated in northern Israel.

🔗 **Read more:** [https://www.aljazeera.com/video/newsfeed/2026/10/12/blast-kills-teenager-injures-dozens-in-northern-israel?traffic_source=rss](https://www.aljazeera.com/video/newsfeed/2026/10/12/blast-kills-teenager-injures-dozens-in-northern-israel?traffic_source=rss)

---

### 9. Photos: Protests over voter lists escalate in India’s capital

**Source:** Al Jazeera

**Category:** world

**Description:**
India’s opposition parties have marched in New Delhi to protest a voter list purge they say favours PM Modi&#039;s party.

🔗 **Read more:** [https://www.aljazeera.com/gallery/2026/10/12/photos-protests-over-voter-lists-escalate-in-indias-capital?traffic_source=rss](https://www.aljazeera.com/gallery/2026/10/12/photos-protests-over-voter-lists-escalate-in-indias-capital?traffic_source=rss)

---

### 10. Wildfire Buckhorn 2, Cassia, Idaho

**Source:** NASA

**Category:** nature

**Description:**
Natural event: Wildfires

🔗 **Read more:** [https://eonet.gsfc.nasa.gov/api/v3/events/EONET_25238](https://eonet.gsfc.nasa.gov/api/v3/events/EONET_25238)

---

### 11. Wildfire PK, Sheridan, Wyoming

**Source:** NASA

**Category:** nature

**Description:**
Natural event: Wildfires

🔗 **Read more:** [https://eonet.gsfc.nasa.gov/api/v3/events/EONET_25233](https://eonet.gsfc.nasa.gov/api/v3/events/EONET_25233)

---

### 12. Wildfire CYRUS, Kern, California

**Source:** NASA

**Category:** nature

**Description:**
Natural event: Wildfires

🔗 **Read more:** [https://eonet.gsfc.nasa.gov/api/v3/events/EONET_25232](https://eonet.gsfc.nasa.gov/api/v3/events/EONET_25232)

---


**Built with ❤️ by GitHub Actions**