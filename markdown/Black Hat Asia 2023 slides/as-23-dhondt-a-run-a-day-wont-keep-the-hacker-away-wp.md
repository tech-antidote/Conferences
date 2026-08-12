---
title: "A Run a Day Wont Keep the Hacker Away"
speakers: ["Dhondt"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Dhondt-A-Run-a-Day-Wont-Keep-the-Hacker-Away-wp.pdf"
pages: 16
sha256: "e1e260ba64f075683f4c4a7fcdab0ad6749141f724e3199c8d6869cb737e57a2"
text_chars: 94379
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T23:53:57Z"
---
# A Run a Day Wont Keep the Hacker Away

**Speakers:** Dhondt  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Dhondt-A-Run-a-Day-Wont-Keep-the-Hacker-Away-wp.pdf` (16 pages)

## Slide 1

# **A Run a Day Won’t Keep the Hacker Away: Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks**

Karel Dhondt

Victor Le Pochat

Alexios Voulimeneas imec-DistriNet, KU Leuven Ghent, Belgium alex.voulimeneas@kuleuven.be

imec-DistriNet, KU Leuven Ghent, Belgium karel.dhondt@kuleuven.be

imec-DistriNet, KU Leuven Leuven, Belgium victor.lepochat@kuleuven.be

Stijn Volckaert

Wouter Joosen imec-DistriNet, KU Leuven Leuven, Belgium wouter.joosen@kuleuven.be

imec-DistriNet, KU Leuven Ghent, Belgium stijn.volckaert@kuleuven.be

## **ABSTRACT**

Networks. In _Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security (CCS ’22), November 7–11, 2022, Los Angeles, CA, USA._ ACM, New York, NY, USA, 16 pages. https://doi.org/10.1145/3548 606.3560616

Fitness tracking social networks such as Strava allow users to record sports activities and share them publicly. Sharing encourages peer interaction but also constitutes a risk, because an activity’s start or finish may inadvertently reveal privacy-sensitive locations such as a home or workplace. To mitigate this risk, networks introduced _endpoint privacy zones_ (EPZs), which hide track portions around protected locations. In this paper, we show that EPZ implementations of major services remain vulnerable to inference attacks that significantly reduce the effective anonymity provided by the EPZ, and even reveal the protected location. Our attack leverages distance information leaked in activity metadata, street grid data, and the locations of the entry points into the EPZ. This yields a constrained search space where we use regression analysis to predict protected locations. Our evaluation on 1.4 million Strava activities shows that our attack discovers the protected location for up to 85% of EPZs. Larger EPZs reduce the performance of our attack, while geographically dispersed activities in sparser street grids yield better performance. We propose six countermeasures, that, however, come with a usability trade-off, and responsibly disclosed our findings and countermeasures to the major networks.

## **1 INTRODUCTION**

Fitness tracking social networks (FTSNs) consistently rank among the most popular mobile apps and saw an additional surge in popularity during the COVID-19 pandemic [4, 51]. For example, one of the largest networks, Strava, has over 100 million registered users [52]. These fitness tracking social networks allow users to record their sports activities, and share their tracks and achievements with friends and other users of the platform, promoting enjoyment and motivation [7]. The tracks represent the routes that the user followed during the activity. While sharing tracks forms part of the attraction of these networks, this, however, comes with privacy and security risks, as they might reveal sensitive information, such as the user’s regular routes or visited locations, to people with ill intentions. Several past incidents drew attention to the dangers of sharing this data with the public, from revealing secret military locations [25], enabling theft of exercise equipment [10], revealing the identity of nearby athletes [47], to doxing users [39].

## **CCS CONCEPTS**

To limit the potential risks of sharing information, all major networks offer privacy controls that limit the amount of shared information, as well as control whom information is shared with. One notable privacy control is the _endpoint privacy zone_ (EPZ). An EPZ allows users to hide track portions near protected (sensitive) locations, such as their home or work address, from all activity tracks shown to other users. This measure aims to prevent harassment and stalking at commonly visited locations [56], or criminal activity such as theft at the protected locations [10]. Most commonly, EPZ implementations balance an increase in privacy with usability, notably in terms of tracking fitness achievements, as features such as leaderboards may only be available for publicly viewable data [14]. Moreover, activities usually still contain the full traveled distance, even for the portions hidden by the EPZ. The user who created the activity can also still access the full activity, as shown in Figure 1.

### • **Security and privacy** → **Privacy protections** ; **Usability in security and privacy** ; **Social aspects of security and privacy** ; **Social network security and privacy** .

## **KEYWORDS**

privacy zones; fitness tracking social networks; location privacy; location-based services; privacy

#### **ACM Reference Format:**

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert. 2022. A Run a Day Won’t Keep the Hacker Away: Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social

This is an extended version that includes the appendices.

This work is licensed under a Creative Commons Attribution International 4.0 License.

One implementation of EPZs hides track portions inside a circle with the sensitive location as its center and a user-configurable radius. However, this implementation has fallen out of favor, as given one or more tracks for one user, it is possible to reconstruct the privacy zone (i.e., the radius) and find the sensitive location

_CCS ’22, November 7–11, 2022, Los Angeles, CA, USA_ © 2022 Copyright held by the owner/author(s).

ACM ISBN 978-1-4503-9450-5/22/11. https://doi.org/10.1145/3548606.3560616

## Slide 2

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert

**Figure 1: Example of an activity in Strava. The interface displays the track** ➀ **, the total traveled distance** ➁ **and accumulated distance at each point (through the elevation profile** ➂ **). Part of the track is marked as ‘hidden’** ➃ **, as it is cloaked by an EPZ. Only the owner of the activity sees that part of the activity is hidden; other users only see the visible part without any indication that another part is hidden.**

(i.e., the center) through basic geometric inference. In 2018, Hassan et al. showed that this EPZ implementation is vulnerable to automated inference attacks [24]. In 2022, Mink et al. showed that human users can visually infer privacy zones that use this implementation [35].

We confirm through a systematic analysis that major fitness tracking social networks implemented some countermeasures in an attempt to better protect sensitive locations from these basic inference attacks [24, 35]. These countermeasures include those proposed by Hassan et al. [24]: larger radii, noise addition at the EPZ boundary, and spatial cloaking where the EPZ center is randomly shifted. However, some usability trade-offs are made, such as allowing small or only fixed radii, or not requiring spatial cloaking. Moreover, some fitness tracking social networks still do not implement EPZs at all.

In this paper, we are the first to show that these newer implementations of EPZs remain highly vulnerable to the discovery of the purportedly protected location, even when countermeasures such as spatial cloaking are applied. Our novel inference attack leverages two inputs that enable a regression analysis resulting in the protected location for an EPZ. First, the road network restricts the possible paths that a user could have taken inside an EPZ. Second, the activity metadata leaks the exact distances of the paths that were traveled inside the EPZ. We then predict the protected location as the point where the distances of the possible and actual paths match best across multiple activities.

We find through an evaluation on 1.4 million real-world Strava activities that our attack can deanonymize protected locations for

up to 85% of EPZs. Larger EPZ radii are more effective at preventing location inference and preserving user privacy, but even for very large radii (1 km), deanonymization remains possible for 55% of EPZs. Through a detailed analysis of the sensitivity of our attack, we find that higher geographic activity diversity and lower street density benefit its performance.

We propose and evaluate six countermeasures that can restore the anonymity of locations protected by EPZs to a varying degree. We find that generalization (rounding) of reported activity distances would be the most effective countermeasure, although it comes with a significant negative usability impact, as fitness tracking social networks are attractive precisely because they allow tracking small achievement differences accurately. Other countermeasures may be less invasive, but are then also less effective at improving privacy. Interestingly, certain interventions such as regenerating EPZs may actually improve our attack’s efficacy, as they provide more data from which the protected location can be more reliably inferred. Countermeasures must therefore be carefully evaluated in order to minimize their negative impact on usability and privacy. We disclosed our findings and proposed countermeasures to the major vulnerable fitness tracking social networks.

In summary, we make the following contributions:

- We conduct a systematic analysis on current EPZ implementations for the most popular fitness tracking social networks.

- We develop a proof-of-concept attack that infers protected locations inside EPZs through regression analysis on the road network and leaked covered distances (Section 4).

- We evaluate our attack on 1.4 million real-world Strava activities (Section 5). We discover sensitive locations for up to 85% of EPZs, and find that our attack performs better with geographically dispersed activities on sparse street grids (Section 6).

- We propose six countermeasures to improve the anonymity provided by EPZs and discuss their trade-offs between privacy and usability (Section 7).

## **2 FITNESS TRACKING SOCIAL NETWORKS**

Our work concerns _fitness tracking social networks_ , where users can record their workouts and share them with others. Users typically record workouts using a GPS-enabled smartphone or wearable device and upload them in the form of _activities_ . An activity contains a _track_ , i.e., the route that the user took, represented by a series of _points_ (coordinates). The activity also reports the total distance traveled, as well as the accumulated distance at each point of the track, along with other metadata such as the duration, pace, elevation profile, heart rate, etc. Finally, many FTSNs define specific stretches of road (e.g., ‘segments’ on Strava) where they maintain a leaderboard of the fastest athletes across these stretches. Figure 1 shows what a fully developed activity may look like.

Most networks offer privacy controls that let users hide all activities from other users (i.e., private profile) or mark specific activities as hidden. Using these controls can severely limit the functionality of social features for the affected activities. For example, activities that are marked as private by their owners cannot be viewed by other users and may be ineligible for inclusion on segment leaderboards and in challenges [7, 14]. However, networks such as Strava

## Slide 3

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks

**Table 1: Number of downloads from the Google Play Store and EPZ features of popular fitness tracking social networks.**

|Application|Downloads|EPZ|EPZ Radii (meter)|
|---|---|---|---|
|Adidas Runtastic [1]|50M+|✗||
|Strava [50]|50M+|circular|[200, ..., 1600] incr 200|
|Garmin Connect [21]|10M+|circular|[100,..., 1000] incr 100|
|Komoot [27]|10M+|polygon||
|Map My Run [55]|10M+|✗||
|Nike Run Club [38]|10M+|✗||
|Relive [42]|10M+|circular|[200,..., 1000] incr 200|
|Ride With GPS [43]|1M+|circular|[150, 300, 600, 1200]|
|Map My Tracks [31]|100k+|circular|[500, 1000, 1500]|

(a) Activity  𝑎 ( { 𝑝 1 , . . . , 𝑝𝑛 } ), as visi- (b) Activity 𝑎 ′ ( { 𝑝 𝑗 , . . . , 𝑝𝑚 } ,  1 ≤
ble to its owner. 𝑗 ≤ 𝑚 ≤ 𝑛 ), as visible to other users.
Activity metadata Total activity distance
total_distance: 1.86,  1.66 km 1.86 km
visible_distances:   0.16 km 1.50 km 0.20 km
 [  0.16 , 0.18,
   ...,    1.65,  1.66  ] 1 j 0.36 km m n
Cloaked distances Visible distance
Inner distance  scenario: 0.16 km + 1.50 km + 0.20 km = 1.86 km
Available distances:
Total distance  scenario: 0.36 km + 1.50 km = 1.86 km

**Figure 2: Visibility of an activity to which an EPZ has been applied. The EPZ is shown as a red circle.**

mark activities as public by default [33] and the majority of users keep this setting [22].

_(Endpoint) Privacy Zones (EPZs)_ are a more functionality-friendly privacy control and are supported by most networks. EPZs allow users to hide the most sensitive parts of the tracks in their activities, as they could otherwise reveal frequently visited locations such as the user’s home or workplace. Activities with EPZs applied to them can still be shared, but the hidden parts of the tracks may still be ineligible for performance comparisons, so users may be inclined to disable or at least severely limit them. We discuss these zones in more detail in Section 3.

## **3 ENDPOINT PRIVACY ZONES**

Most FTSNs allow their users to hide a privacy-sensitive location by letting them define an _Endpoint Privacy Zone_ (EPZ) around that location. One location corresponds to exactly one EPZ, but a user can configure multiple locations that each have their own EPZ. EPZs can be regenerated at any time and are applied retroactively to all the activities of the owner. The goal of the EPZ is then to hide

those parts of the track that might reveal the sensitive location, i.e., are near this location. Only the owner of the activity _𝑎_ can view the full track, including its _actual_ start and finish points (together the ‘endpoints’), as well as the layout of the EPZ itself (shown in Figure 2a). Other users only see a cloaked activity _𝑎_<sup>′</sup> as defined in Definition 1 and depicted in Figure 2b. Concretely, in such a cloaked activity all points from the start of the track until the first time the owner leaves the EPZ are hidden, as are all points from the last time the owner enters the EPZ until the end of the track. The other users therefore observe _cloaked_ start and finish points. Note that if the owner passes through the EPZ but does not start or end there, that track portion through the EPZ is not hidden. Moreover, even though the points inside the EPZ are hidden, the accumulated distance for points outside the EPZ as well as the total distance are not changed. This forms the basis for our attack described in Section 4.

**Definition 1** (Endpoint Privacy Zone) **.** Let protected location _𝑝𝑠_ = ( _𝑥𝑠,𝑦𝑠_ ) be a point in the Cartesian plane _𝐶_ , and _𝑎_ be an activity route of _𝑛_ points { _𝑝_ 1 _, . . . , 𝑝𝑛_ }. We denote _𝑝_ 1 as the actual start point and _𝑝𝑛_ as the actual finish point.

Let _𝐸𝑃𝑍_ be a subplane of _𝐶_ . Enforcing _𝐸𝑃𝑍_ on activity _𝑎_ results in a cloaked activity _𝑎_<sup>′</sup> = { _𝑝 𝑗 , . . . , 𝑝𝑚_ } with 1 ≤ _𝑗_ ≤ _𝑚_ ≤ _𝑛_ , where _𝑝 𝑗_ is the first point and _𝑝𝑚_ the last point of the activity route that does not lie in _𝐸𝑃𝑍_ . We denote _𝑝 𝑗_ as the cloaked start point and _𝑝𝑚_ as the cloaked finish point.

In Table 1, we list the supported EPZ parameters of popular FTSNs. Most FTSNs use circular EPZs and let the user select the radius of the circle from a set of fixed radii. Hassan et al. inferred protected locations using publicly available information such as the advertised start and finish point of the user’s activity [24]. The researchers demonstrated that, given multiple endpoints of protected activities and the circular layout of the EPZ, an adversary could reconstruct the EPZ and expose the protected location (i.e., the center point of the EPZ). To deal with the aforementioned attack, some FTSNs apply _spatial cloaking_ by adding a random translation to the center of the EPZs [23], resulting in a cloaked circular EPZ as defined in Definition 2. An adversary could still determine the parameters of the cloaked EPZ, but cannot infer the protected location, since the protected location and the EPZ center do not match. Komoot uses a randomly shaped polygon around the protected location, rather than a circular EPZ. This makes it more difficult for an attacker to deduce the shape of the privacy zone [28]. Map My Tracks has an automatic privacy zone detection tool, lowering the bar for users to create a privacy zone [37]. This automatic tool scans all new activity endpoints in order to identify regular start and finish locations. If such locations are detected, a (circular) EPZ is enforced on all activities retroactively. This feature is enabled by default but can be disabled by the user at any time.

**Definition 2** (Cloaked Circular Endpoint Privacy Zone) **.** Let _𝑐𝐸𝑃𝑍_ be a circle with a center _𝑝𝑠𝑡𝑟𝑎𝑛𝑠_ randomly translated from protected location _𝑝𝑠_ , and radius _𝑅_ . Enforcing _𝑐𝐸𝑃𝑍_ on activity _𝑎_ results in an cloaked activity _𝑎_<sup>′</sup> = { _𝑝 𝑗 , . . . , 𝑝𝑚_ } with 1 ≤ _𝑗_ ≤ _𝑚_ ≤ _𝑛_ , where _𝑝 𝑗_ is the first point where dist( _𝑝 𝑗 , 𝑝𝑠𝑡𝑟𝑎𝑛𝑠_ ) _> 𝑅_ , and _𝑝𝑚_ the last point where dist( _𝑝𝑚, 𝑝𝑠𝑡𝑟𝑎𝑛𝑠_ ) _> 𝑅_ .

## Slide 4

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

**Figure 3: The intuition behind our attack: we search the protected location (shown as a black marker) as the point where the theoretical paths (based on reported distances, shown by dashed lines) starting from the EPZ entry gates (in different directions, shown by different colors) intersect.**

## **4 BREAKING ENDPOINT PRIVACY ZONES**

In this section, we present an attack against the current state-of-theart EPZs under a predefined threat model. Crucially, this attack is enabled by the availability of exact accumulated and total distances for cloaked activities, revealing the distance traveled inside the EPZ. The intuition behind our attack is that if a victim has multiple activities in one or more cardinal directions (which we denote as ‘entry gates’), we can use these distances to limit the locations where the victim could have started or ended their activities. For example, consider the three activities in Figure 3 indicated in blue, orange and green. While only the owner of the activities can see the dashed portions of the activities inside the EPZ, the attacker still knows their lengths. With these lengths and given the street grid, an adversary is able to construct all paths the victim could have covered inside the EPZ. Given these paths, the endpoint of the activities is at risk of being inferred using the intersection of multiple distinct paths inside the EPZ. We divide the breaking of privacy zones into two subproblems: first, identifying EPZs to reduce the search space, and second, finding the protected location inside those EPZs through regression analysis.

## **4.1 Threat Model**

For this work, we consider an attacker who attempts to infer the protected locations of another user by only using the publicly available information that a regular user would be entitled to view, as displayed by the FTSN. The adversary has exactly the same rights as a regular user and cannot access any information by any other means, e.g., by infiltrating the FTSN’s servers. The attacker can target either one specific user or the entire userbase of the network.

The attacker is reasonably technically sophisticated, capable of inspecting network traffic to retrieve the activity metadata (e.g., in

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert

browser developer tools), download map data and run the inference algorithm. This attacker model is similar to that of Hassan et al. [24]. Mink et al. [35] consider a less technically skilled attacker, who infers protected locations visually from the activity view on the network’s website. In the context of intimate partner violence, Tseng et al. [54] found evidence of forum discussions where users collaborate on technically sophisticated attacks. Given possibly similar motivations to deanonymize protected locations (e.g., stalking), even less technically skilled attackers could receive support in successfully deploying the inference attack.

## **4.2 Identifying EPZs**

As a preliminary step for our attack, we seek to identify the EPZs of a user. This step resembles the attack developed by Hassan et al. [24], where identifying the EPZ (by fitting a circle) reveals the protected location. However, this is no longer sufficient for our inference attack, as networks use EPZs with countermeasures against Hassan et al.’s attack. In our case, this step is also not strictly necessary for our attack to be effective, as we can search candidate locations throughout the entire street grid regardless of the EPZ layout. However, this step constrains the search space, which improves the attack’s efficacy and computational performance by removing points that are ineligible as protected location. Moreover, if one search space contains multiple non-overlapping EPZs<sup>1</sup> , our regression-based approach for location discovery (see Algorithm 2) may return a location outside these EPZs, i.e., in fact ineligible to be a protected location. Some restriction is therefore advantageous, although it does not need to be precise. Nevertheless, with knowledge of how EPZs are configured on a specific platform (see Section 3), the adversary can identify the distinct EPZs more precisely.

As an example of an EPZ identification algorithm, we present Algorithm 1 that discovers circular EPZs. Such EPZs are used by most services (Table 1). This algorithm identifies multiple circular EPZs, each with different protected locations and parameters, from the set _𝐴_ of all cloaked activities of one user. The input to our algorithm is the set _𝑃_ of all start points _𝑝 𝑗_ for cloaked activities that started inside an EPZ and all finish points _𝑝𝑚_ for activities that ended in an EPZ, as they are shown to the adversary (a non-owner user)<sup>2</sup> . We then adapt the _𝑘_ -means clustering algorithm [30] to output the distinct circular EPZ layouts based on these start and finish points, iteratively increasing _𝑘_ until every EPZ is represented by exactly one cluster. For a given _𝑘_ , the algorithm initializes _𝑘_ clusters _𝑆𝑖_ ( _𝑖_ = 1 _, . . . ,𝑘_ ) with randomly selected points from _𝑃_ . In subsequent iterations, our algorithm assigns each point _𝑝_ to the cluster _𝑆𝑖_ with the lowest Euclidean distance to the least squared circle _𝐶𝑖_ fitted between the points of that cluster, and fitted such that none of the points lay inside _𝐶𝑖_ (a circular EPZ cloaks all points within the circle, cf. Definition 2). This cost function differs from regular _k_ -means, where the distance from points to the mean of their cluster is minimized. The radius of the fitted circle should be bounded by the notion of the minimum and maximum radius of an

> 1In case the EPZs overlap, we consider the union as one EPZ with multiple protected locations. Bootstrapping the activities for the input to Algorithm 2 will then probabilistically return these two locations (see also Section 6.2).

> 2Note that we convert the geodetic coordinates (latitude and longitude) from the FTSN activity data, to plane coordinates (Universal Transverse Mercator) by projecting them onto a Cartesian plane, as established in Definition 1.

## Slide 5

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks

|**Algo **|**rithm 1**cEPZ identification algorithm|
|---|---|
|**Inpu**|**t:**
|
|_𝑃_|_⊲_Set of endpoints for cloaked activities|
|**Outp**|**ut:** _𝐶_1_,...,𝑘_=_𝑐𝐸𝑃𝑍_1_,...,𝑘_
_⊲𝑘_cEPZs|
|1: **p**|**rocedure**cEPZ identification(_𝑃_)
|
|2:|_𝑘_←1|
|3:|**do**
|
|4:|Initialize_𝑘_clusters_𝑆𝑖_<sup>3 </sup>at random (_𝑖_=1_, . . . ,𝑘_)|
|5:|**do**|
|6:|_⊲_Assignment step|
|7:|**for**point_𝑝_in_𝑃_**do**|
|8:|_𝑖_←argmin_𝑖_dist(_𝑝,𝐶𝑖_)|
|9:|_𝑆𝑖_=_𝑆𝑖_∪{_𝑝_}|
|10:|**end for**|
|11:|_⊲_Update step|
|12:|**for**cluster_𝑆𝑖_in_𝑆_**do**|
|13:|_𝐶𝑖_←LSQ fit circle through{_𝑝_|_𝑝_∈_𝑆𝑖_}|
|14:|**end for**|
|15:|**while**∃_𝐶𝑖_: centroid change of_𝐶𝑖> 𝜏𝑐𝑜𝑛𝑣𝑒𝑟𝑔𝑒𝑑_|
|16:|_𝑘_←_𝑘_+1|
|17:|**while**∃_𝑝_∈_𝑆𝑖_: dist(_𝑝,𝐶𝑖_) _> 𝜏𝑑𝑖𝑠𝑗𝑜𝑖𝑛𝑡_|
|18:|**return**_𝐶_1_,...,𝑘_|
|19: **e**|**nd procedure**|

EPZ implementation. This avoids too small clusters ‘overfitted’ on too few points such that multiple circles actually are part of one EPZ, and too large clusters due to outlier points.

Our algorithm repeats these assignments of points to clusters and updates to fitted circles until the circles’ centroid changes between iterations are all lower than _𝜏𝑐𝑜𝑛𝑣𝑒𝑟𝑔𝑒𝑑_ . This threshold should be (empirically) selected such that clusters are sufficiently stable while not indefinitely updating clusters. Moreover, _k_ -means might return a local instead of global minimum because of the random assignment of points to clusters during the initialization phase. In practice, our algorithm will therefore repeat the initialization, assignment and update steps several times and use the clusters with the lowest distortion, i.e., the global squared sum of distances between points and the edge of their assigned fitted circle.

The algorithm finally checks whether all distinct EPZs have been identified, or whether multiple EPZs are still merged into one cluster. It therefore tests whether the maximum distance of every point _𝑝_ to its assigned fitted circle (EPZ) is lower than _𝜏𝑑𝑖𝑠𝑗𝑜𝑖𝑛𝑡_ . This threshold could, for example, be the known maximum radius for the specific EPZ implementation. If this is not yet the case, we assume there is still a cluster containing multiple EPZs, and therefore increment _𝑘_ to add a cluster and restart at the random assignments of points to clusters. Once the condition on _𝜏𝑑𝑖𝑠𝑗𝑜𝑖𝑛𝑡_ is also met, the algorithm outputs the fitted circles _𝐶_ 1 _,...,𝑘_ through the points of each cluster _𝑆𝑖_ , which correspond to the _𝑘𝑐𝐸𝑃𝑍_ s configured by the user.

## **4.3 Finding the Protected Location for an EPZ**

The core of our attack consists of predicting protected locations for each individual EPZ previously identified by the adversary. We associate this EPZ with the subset of user activities _𝐴𝐸𝑃𝑍_ that

> 3with corresponding circles _𝐶𝑖_

**Algorithm 2** Protected location prediction algorithm

|**Inpu**|**t:**|
|---|---|
|_𝐺_|_𝐸𝑃𝑍_= (_𝑉, 𝐸_)
_⊲_Road graph inside EPZ|
|_𝐴_|_𝐸𝑃𝑍_= (_𝑃,𝑂_)
_⊲_Endpoints and distances inside EPZ|
|**Outp**
|**ut:** _𝑣𝑝𝑟𝑜𝑡𝑒𝑐𝑡𝑒𝑑_
_⊲_Predicted protected location
|
|1: **p**|**rocedure**predict protected locations(_𝐴_,_𝐺_)|
|2:|_⊲_Calculate theoretical distances|
|3:|_𝐴_<sup>′ </sup>←∅|
|4:|**for**pair(_𝑝𝑙,𝑜𝑙_) in_𝐴_**do**|
|5:|_𝑣𝑝𝑙_←argmin_𝑣_∈_𝑉_dist(_𝑝𝑙, 𝑣_)
|
|6:|_𝑑𝑝𝑙_←dist(_𝑝𝑙, 𝑣𝑝𝑙_)|
|7:|**if**_𝑑𝑝𝑙_≤_𝜏𝑠𝑛𝑎𝑝_**then**|
|8:|_𝐴_<sup>′ </sup>←_𝐴_<sup>′ </sup>∪{(_𝑣𝑝𝑙,𝑜𝑙_)}|
|9:|**end if**|
|10:|**end for**|
|11:|_𝑇_←|_𝐴_<sup>′</sup>| × |_𝑉_|matrix|
|12:|**for**pair(_𝑣𝑝𝑙,𝑜𝑙_) in_𝐴_<sup>′</sup> **do**|
|13:|_𝑇𝑣𝑝𝑙,_∗←dijkstra_single_source_lengths(_𝑣𝑝𝑙,𝐺_)|
|14:|**end for**|
|15:|_⊲_Identify entry gates_𝑌_|
|16:|_𝑌_←_𝐷𝐵𝑆𝐶𝐴𝑁_(_𝐴_<sup>′</sup>_,𝜖,𝑚𝑖𝑛𝑃𝑡𝑠_)|
|17:|_⊲_Remove deviating activities|
|18:|_𝐴_<sup>′′ </sup>←∅|
|19:|**for**entry gate_𝑌𝑖_= (_𝑃𝑖,𝑂𝑖_) ⊆_𝐴_<sup>′ </sup>in_𝑌_**do**|
|20:|_𝑌_<sup>′</sup>
_𝑖_<sup>←{(</sup><sup>_𝑣𝑝𝑙,𝑜𝑙_)|(</sup><sup>_𝑣𝑝𝑙,𝑜𝑙_) ∈</sup><sup>_𝑌𝑖,𝑜𝑙_≤max(</sup><sup>_𝑇𝑙,_∗)}</sup>|
|21:|_𝑌_<sup>′′</sup>
_𝑖_
←{(_𝑣_<sup>′</sup>_𝑝𝑙,𝑜_<sup>′</sup>
_𝑙_<sup>)|(</sup><sup>_𝑣_′</sup><sup>_𝑝_</sup>_𝑙_<sup>_,𝑜_′</sup>
_𝑙_<sup>) ∈</sup><sup>_𝑌_′</sup>
_𝑖_<sup>_,_ |</sup><sup>_𝑜_′</sup>
_𝑙_<sup>−</sup>
_𝑂_<sup>′</sup>
_𝑖_<sup>| ≤3</sup><sup>_𝜎𝑂_′</sup>
_𝑖_<sup>}</sup>|
|22:|_𝐴_<sup>′′ </sup>←_𝐴_<sup>′′ </sup>∪_𝑌_<sup>′′</sup>
_𝑖_|
|23:|**end for**|
|24:|_⊲_Predict protected location

|
|25:|_𝑣𝑝𝑟𝑜𝑡𝑒𝑐𝑡𝑒𝑑_←argmin_𝑣𝑙_∈_𝑉_
�
(_𝑣_<sup>′′</sup>_𝑝𝑙,𝑜_<sup>′′</sup>
_𝑙_<sup>)∈</sup><sup>_𝐴_′′</sup>
���_𝑜_′′
_𝑙_<sup>−</sup><sup>_𝑇𝑣_′′</sup>_𝑝𝑙_<sup>_,𝑣𝑙_</sup>
���|
|26:
27: **e**|**return**_𝑣𝑝𝑟𝑜𝑡𝑒𝑐𝑡𝑒𝑑_
**nd procedure**|

were cloaked using this EPZ (cf. Definition 1). We then retrieve the road network graph _𝐺𝐸𝑃𝑍_ inside the EPZ, defined as a set of edges _𝐸_ through nodes _𝑉_ that represent all the possible protected locations. This effectively constrains our search space to a finite set of locations, and therefore reduces the identification of the protected location inside an EPZ from a continuous to a discrete problem. The correctness of our solution is therefore also limited by the resolution of the graph _𝐺_ . This resolution can be improved using _chaining_ , i.e., adding equidistant, intermediate nodes at a certain interval distance _𝑑𝑐ℎ𝑎𝑖𝑛_ , e.g., selected to mimic GPS precision, on edges longer than _𝑑𝑐ℎ𝑎𝑖𝑛_ as depicted in Figure 4b.

We propose Algorithm 2 that predicts the most probable candidate based on two inputs. The first input is the previously constructed road graph _𝐺_ with nodes _𝑉_ and edges _𝐸_ . The second input is the set of cloaked activities _𝐴𝐸𝑃𝑍_ , as defined by a mapping from the union of their cloaked start ( _𝑝 𝑗_ ) and finish ( _𝑝𝑚_ ) points _𝑃_ , to the reported distances _𝑂_ between the actual and cloaked start points (dist( _𝑝_ 1 _, 𝑝 𝑗_ )) or the actual and cloaked finish points (dist( _𝑝𝑚, 𝑝𝑛_ )), respectively. These reported distances are available through the activity data (e.g., elevation profile). In our _inner distance_ scenario, the distances for the start and finish point are available separately, as the accumulated distance from the beginning at the cloaked start

## Slide 6

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert

point and the remaining distance until the end from the cloaked finish point respectively. We generalize this to a _total distance_ scenario in which only the combined cloaked distance is available, i.e., without distinct distances for the start and finish point. If only one of the points lies inside a privacy zone (as could be inferred using Algorithm 1), the total distance trivially reduces to the inner distance, as this inner distance at the single cloaked side is equal to the reported distance discrepancy. Our data characteristics in Section 5.2 show that 35.08% of activities only start or finish inside an EPZ, but not both. When both endpoints are cloaked, there is an unresolvable degree of freedom in the division of the distance discrepancy over the start and finish points. In this case, the activity is discarded, and the attack is run on the remaining activities. Our analysis in Section 6.3 shows that our attack still performs well in this total distance scenario, with only a minor performance reduction compared to the inner distance scenario.

In an ideal context, the endpoints for the reported distances of all activities would overlap at exactly one node of the road graph (i.e., the protected location) if the following idealistic assumptions were to hold:

- A1. The cloaked start and finish points intersect with the edge of the EPZ.

- A2. A protected location is always located along a path, i.e., on a node inside _𝐺_ .

- A3. The victim starts and finishes their activity at the single protected location inside a distinct EPZ.

- A4. Inside the EPZ, the victim uses the shortest path on the street grid from or to the protected location.

However, in practice these assumptions do not always hold. For example, a user might only start recording their activity 50 meters away from their protected location, and GPS tracking errors will cause a track to deviate from (the shortest path on) the street grid. Overall, for a 200m EPZ, 54% of all activities in our real-world data set (Section 5) violate at least one idealistic assumption. Our approach is explicitly designed to be robust against these violations, i.e., it works even in non-ideal settings. We develop a four-step algorithm that provides a sufficiently correct solution even though these assumptions from the ideal context do not hold, as we show in our real-world evaluation (Section 6).

_4.3.1 Calculate Theoretical Distances._ The algorithm starts by map matching (‘snapping’) all endpoints to the road graph. For each point _𝑝𝑙_ ∈ _𝑃_ , the algorithm identifies the node _𝑣𝑝𝑙_ ∈ _𝑉_ with the lowest Euclidean distance _𝑑𝑝𝑙_ to _𝑝𝑙_ . If this distance exceeds a threshold _𝜏𝑠𝑛𝑎𝑝_ , the algorithm discards this point since it is uncertain if the road was used. _𝜏𝑠𝑛𝑎𝑝_ could be empirically selected based on the mean GPS sampling distance. _𝑃_<sup>′</sup> represents the set of map matched points _𝑣𝑝𝑙_ that are retained. The algorithm then computes the shortest path lengths from _𝑣𝑝𝑙_ (recall: a point near the edge of the EPZ) to all other nodes _𝑉_ inside the EPZ using the Dijkstra single source multiple destination algorithm [16]. The lengths are collected into a distance matrix _𝑇_ of size | _𝑃_<sup>′</sup> | × | _𝑉_ |. These lengths represent the ‘theoretical’ distances from the cloaked map matched endpoints at the edge of the EPZ to nodes within the EPZ (i.e., possible protected locations), if the track were to exactly follow the road graph. However, GPS errors and the variation across the width of a road cause the actual user tracks to deviate from this road graph. The

**(a) Example road network graph** _𝐺_ **for (b) Road network with node resolution one EPZ. increased through chaining.**

**Figure 4: The road network graph** _𝐺_ **constrains the search space for our location prediction algorithm. Each node** _𝑣_ ∈ _𝑉_ **, displayed in red, is a potential protected location.**

(a) (b) (c)

**Figure 5: Entry gates are identified as clusters of close endpoints. Endpoints will not exactly intersect the circular EPZ, as the first (last) point outside the EPZ will be the first (last) visible point. No endpoints therefore lie inside the EPZ.**

regression analysis in the last step of our algorithm addresses these deviations when predicting the protected location.

_4.3.2 Identify Entry Gates._ The exact intersection point of an activity and the EPZ is seldom recoverable, violating Assumption A1. Definition 1 states that the activity gets cut off at the first point outside the EPZ rather than at the exact intersection. In combination with low GPS sampling rates (to save battery) and GPS errors, this cloaked endpoint can be distant from the edge of the EPZ, particularly as the speed of an activity increases. Figure 5 shows an example of this scenario, where the endpoints of an activity do not exactly intersect with the circular EPZ.

We cluster the cloaked endpoints _𝑝𝑙_ to form dense regions. We refer to these regions as _entry gates_ , and we assume that each entry gate _𝑌𝑗_ consists of endpoints _𝑃𝑌𝑗_ ⊆ _𝑃_<sup>′</sup> where the intersection point of the actual track with the edge of the EPZ is shared. In Figure 5, the points that form one entry gate are displayed in the same color. The most suitable algorithm for geospatial data is DBSCAN [19], a density-based clustering algorithm, since it does not require a priori knowledge of the number of clusters (i.e., entry gates). DBSCAN requires two parameters: _𝜖_ , the maximum distance between two points of the cluster, and _𝑚𝑖𝑛𝑃𝑡𝑠_ the minimum number of points to form a dense region. For example, _𝜖_ could be determined as the 95th

## Slide 7

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks

quantile of sample distances (i.e. distances between consecutive activity points). We run DBSCAN on the points _𝑃_<sup>′</sup> to obtain all entry gates _𝑌_ , each defined by a subset _𝑃𝑌𝑗_ ⊆ _𝑃_<sup>′</sup> of the points corresponding to that entry gate, disjoint with all other subsets.

_4.3.3 Remove Deviating Activities._ Next, we discard outlier endpoints that could incorrectly skew the prediction of the protected location. Such outliers may stem from activities where the user started or finished far away from the protected location (violating Assumption A3), or did not follow the shortest path within the EPZ (violating Assumption A4).

The algorithm starts by discarding points _𝑣𝑝𝑙_ with a reported distance _𝑜𝑙_ larger than the maximum theoretical distance _𝑇𝑙,_ max from _𝑣𝑝𝑙_ to a node inside the EPZ, i.e., the maximum of the matrix row _𝑇𝑙,_ ∗. We do this because these activities could never cover the shortest path towards the protected location. For each entry gate _𝑌𝑗_ , our algorithm then discards outlier points where the reported distance deviates significantly from the distance for other points within the same entry gate. Concretely, we consider a deviation of more than three standard deviations from the mean significant.

_4.3.4 Predict Protected Location._ As the points that constitute one entry gate do not overlap exactly, we use least absolute deviation (LAD) regression to predict the most likely protected location across all these diffuse entry gates. For each node _𝑣𝑙_ inside the EPZ (i.e., each possible protected location), the algorithm calculates the sum of absolute differences across all points _𝑣𝑝𝑙_ ∈ _𝑃_<sup>′</sup> between the observed distance _𝑜𝑙_ and the theoretical shortest path distance _𝑇𝑣𝑝𝑙 ,𝑣𝑙_ between _𝑣𝑝𝑙_ and _𝑣𝑙_ . The final predicted protected location is then the node _𝑣𝑙_ ∈ _𝑉_ where this sum is minimal. Note that we retain Assumption A2 here, as the predicted location will always be located on the road graph. However, users may start or finish their activity away from the road, e.g., on their private grounds. We offset this violation of our assumption through the definition of an error threshold _𝜏𝑒_ , below which the protected location is sufficiently closely predicted to deanonymize the user. In Appendix A, we empirically determine an acceptable error threshold based on real-world activities.

## **5 DATA COLLECTION**

A large pool of real user data from a fitness tracking social network is required to further evaluate the plausibility of our attack against state-of-the-art EPZ implementations. For this, we use Strava because it is one of the most popular fitness tracking social networks, with over four billion total activities recorded so far [51]. In this section, we explain the methodology we used to collect user data from Strava and further analyze this data set to obtain useful insights into the privacy habits of users and fitness trackers.

## **5.1 Methodology**

The scope of our data collection is a period of one week starting from 11 July 2021. By inspecting timestamps and elapsed time of activities, we conclude that IDs of activities are assigned sequentially rather than randomly upon uploading. However, due to delays in uploading activities to Strava, the temporal order is not sequential. We identify the first activity ID globally assigned after 11 July 2021 00:00 UTC. We then visit each next 9,000th public activity from approximately 36 million activities uploaded during this week. If

**Table 2: Empirically selected parameters for Algorithms 1 and 2, and the success rate metric, as used in our evaluation.**

|**(a) Algorit**|**hm 1**||**(b) Algo**|**rithm 2**||**(c) Success rate**|
|---|---|---|---|---|---|---|
|Parameter|Value|Param.|Value|Param.|Value|Param.
Value|
|_𝜏𝑐𝑜𝑛𝑣𝑒𝑟𝑔𝑒𝑑_|10 m|_𝑑𝑐ℎ𝑎𝑖𝑛_|3 m|_𝑚𝑖𝑛𝑃𝑡𝑠_|1|_𝜏𝑒_
22.95 m|
|_𝜏𝑑𝑖𝑠𝑗𝑜𝑖𝑛𝑡_|1600 m|_𝜏𝑠𝑛𝑎𝑝_|10 m|_𝜖_|20 m||

this activity is not public, does not exist anymore, or was completed before 11 July but only uploaded after, we consider the next sequential activity. For this (public) activity, we identify the user who created it. This ultimately provides us with a randomly generated, representative sample of 4,000 users.

For each user in our sample, we retrieve user information (i.e., nationality) and the IDs of their public activities with map data. For this, we scrape and parse the _overview_ section of the athlete’s profile page<sup>4</sup> using Selenium [49]. Then, for each activity (ID), we extract its total distance and type from the strava.com/activities/ID page. We also collect the elevation profile including the GPS track points as coordinate pairs with the corresponding elevation and accumulated distance data from the strava.com/stream/ID API endpoint. Since an authenticated user can make a maximum of 375 requests to Strava’s stream API per day, we use multiple accounts to speed up the download process. Despite downloading with multiple accounts to circumvent rate limiting, our data set took three months to collect. Before storing our collected data in our database, we pseudonymized the data by replacing original user IDs with an autoincremented primary key upon request of our IRB. We repeat the same procedure for activity IDs.

To obtain the road graph for each EPZ, we use the OSMnx framework [8] to download the OpenStreetMap road network in a graph format (see Figure 4a).

## **5.2 Data Characteristics**

With the aforementioned methodology, we collected a data set of 1,404,886 activities created by 4,000 users. We plot several distributions within this data set in Appendix B. The distribution of number of activities per user is shown in Figure 11, with a median of 136 activities per user. Our data set is geographically diverse as shown in Figure 12, containing activity endpoints from 160 different countries. The data set provides different densities and layouts of road networks, which is an important factor for the efficacy of our attack as shown in Section 6.4.4.

We observe that 461 users (11.53% of our total data set) use at least one EPZ to cloak activities. Figure 13 shows the distribution of EPZ radii for these users, as determined through Algorithm 1 (with parameters from Table 2a). Radii up to 400m have a 65.50% share, indicating that smaller radii are more popular than larger ones. 35.08% of protected activities in our data have only one cloaked endpoint, making them usable for the total distance scenario. We observe non-fixed EPZ radii in our data set that have a statistically insignificant distortion score and fit the endpoints well through visual inspection. We assume that user-selected, non-fixed radii are a legacy feature that is not available anymore.

4strava.com/athletes/ATHLETE_ID

## Slide 8

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert

## **6 EVALUATION**

## **6.1 Ground Truth Definition**

To assess the effectiveness of our algorithm, we require a ground truth of known protected locations that we can compare to the predictions made by our algorithm. To do so, we use the 1,312,250 uncloaked<sup>5</sup> activities generated by the 4,000 users in our data set (Section 5). For each user, we search their activities that are part of clusters of at least 15 endpoints that fall within 50 meters of one another. Since most fitness tracking social networks use an autocomplete address form for the creation of privacy zones, we then designate the streetside location of the closest address to these cluster’s centroids as our ground-truth location _𝑣𝐺𝑇_ ∈ _𝑉_ (i.e., the point that a user would configure as a protected location). We believe that inferring likely protected locations from uncloaked activities is the most feasible way to generate a sufficiently large-scale yet reliable ground truth. We note that our approach to obtaining ground truth is almost identical to that of the existing state of the art [24].

Using the aforementioned methodology, we constructed 4,689 ground-truth locations for 2,527 users (63.18 % of entire data set). We were unable to construct at least one reliable ground-truth location for the other 1,473 users due to a lack of geographically concentrated, uncloaked activities of the _Walk_ , _Run_ or _Ride_ type.

## **6.2 Prediction Evaluation**

For each ground-truth location, we synthesize an EPZ, with its center randomly translated from that location, for each radius in the set of radii available in Strava. We consider this set of radii as exemplar since Strava is one of the most popular FTSNs, and since it supports the largest EPZ radii. In the case that multiple protected locations of the same user are located inside the same EPZ, i.e., closer to each other than the EPZ radius (8% of 200m EPZs), we only synthesize an EPZ around the protected location with the most activity observations. We then simulate the cloaking of these –previously uncloaked– activities by removing all points that fall within the synthetic EPZ. Finally, we evaluate our attack by predicting the corresponding protected location of each (synthesized) EPZ using Algorithm 2 with the locally cloaked activity data as input. We then compare this prediction (i.e., the result of our algorithm) with the ground-truth location.

We measure the predictive error of Algorithm 2 by constructing confidence intervals (CIs) using bootstrapping [18], a random sampling method with replacement. We run our algorithm (using the parameters in Table 2b) 1000 times with resampled data from the observed activities _𝑎_ , retaining the original number of cloaked activities for this EPZ. This yields 1000 (not necessarily distinct) predicted locations _𝑉𝑝𝑟𝑒𝑑_ ⊆ _𝑉_ , which we denote as the CI constructed by bootstrapping. This finally allows us to estimate the probability distribution _𝑃𝑟_<sup>�</sup> ( _𝑣_ | _𝑎_ ), i.e., protected locations _𝑣_ ∈ _𝑉_ given the user’s activities _𝑎_ , with the probability quantified as the number of times the location was predicted out of the 1000 runs of our algorithm. Note that this probability is, therefore, zero for locations that were never predicted, i.e., _𝑣𝑝_ ∈ _𝑉𝑝𝑟𝑒𝑑_ ⇔ _𝑃𝑟_<sup>�</sup> ( _𝑣𝑝_ | _𝑎_ ) _>_ 0. We compute an extended CI _𝑉𝑝𝑟𝑒𝑑,𝑒𝑥𝑡_ ⊆ _𝑉_ to account for the ‘overshoots’ caused

5While FTSNs do not explicitly show that an EPZ is used, we infer whether an activity is cloaked by checking if there is a discrepancy in the visible distance and total distance of an activity.

by activities starting or finishing away from the road graph (Section 4.3.4). This extended CI encompasses the nodes _𝑣𝑒_ ∈ _𝑉_ that lie within the error threshold _𝜏𝑒_ of the predicted locations _𝑉𝑝𝑟𝑒𝑑_ , i.e., _𝑣𝑒_ ∈ _𝑉𝑝𝑟𝑒𝑑,𝑒𝑥𝑡_ ⇔∃ _𝑣𝑝_ ∈ _𝑉𝑝𝑟𝑒𝑑_ : dist( _𝑣𝑒, 𝑣𝑝_ ) ≤ _𝜏𝑒_ . We further discuss the overshoots, and empirically determine _𝜏𝑒_ in Appendix A.

We subject our predictions to the following privacy metrics, which except for success rate, we compute separately for each EPZ:

_Success rate_ [36] is defined as the percentage of EPZs for which the attacker is ‘successful’ (binary value). An attacker is considered succesful when the ground-truth location lays inside the extended CI _𝑉𝑝𝑟𝑒𝑑,𝑒𝑥𝑡_ or, in other words, the predicted protected location is sufficiently close to the ground-truth location to deanonymize the user.

_Correctness_ [48] is quantified as the sum of Euclidean distances between the true outcome (ground-truth location) _𝑣𝐺𝑇_ and each node _𝑣_ ∈ _𝑉_ , weighted by the probability distribution _𝑃𝑟_<sup>�</sup> ( _𝑣_ | _𝑎_ ) (nonzero only if the location was predicted).

_Accuracy_ [48] is quantified as the width of the confidence interval constructed by bootstrapping (i.e., the number of unique predicted locations _𝑣𝑝𝑟𝑒𝑑_ ). Note that a higher value for accuracy reflects a wider confidence interval, so the adversary is less confident of their prediction, and privacy improves.

_Reduction of the 𝑘-anonymity set_ refers to the _𝑘_ -anonymity set [44, 45, 53] generated by an EPZ covering a ground-truth location, with _𝑘_ the number of nodes of the chained road graph inside the EPZ (i.e., all possible protected locations). The reduction is then defined as the proportion of _𝑘_ minus the number of nodes inside the extended CI, over _𝑘_ .

_Size of Uncertainty Region_ [13] is defined as the area of the union of (possibly disjoint) circles around the predicted nodes in the confidence interval with a radius equal to the chaining distance.

_Certainty_ [48] is the Shannon entropy [46] of the estimate distribution _𝑃𝑟_<sup>�</sup> ( _𝑣_ | _𝑎_ ) and represents how concentrated the probability distribution is, but lacks a notion of (spatial) neighborhoods. A higher entropy value indicates a less certain adversary.

_Spatial Certainty_ is based on Karlstrom and Ceccato’s entropy [26]. Instead of using the probability of a single node _𝑣_ , we use the logarithm of the neighborhood probability _𝑃𝑟_<sup>�</sup> _𝑛_ ( _𝑣_ | _𝑎_ ) as the surprisal term of the entropy formula. Therefore, this represents how _spatially_ concentrated the distribution is. We refer the reader to Section 11 for more details on this new metric.

## Slide 9

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks

**Table 3: Susceptibility to our attack of popular FTSNs’ EPZ implementations, for the two scenarios from Section 4.3.**

|Application|Inner|Total|
|---|---|---|
|Strava [50]|✓|✓|
|Garmin Connect [21]|✗|✓|
|Relive [42]|✗|✗|
|Komoot [27]|✗|✓|
|Map My Tracks [31]|✓|✓|
|Ride With GPS [43]|✓|✓|

_Degree of Anonymity_ [15] is the entropy of the estimate distribution _𝑃𝑟_<sup>�</sup> ( _𝑣_ | _𝑎_ ), normalized by the maximum value entropy _𝐻_ 0 ( _𝑉_ ) when all nodes inside the EPZ are equally likely.

## **6.3 Results**

In this subsection, we present the results of our attack against actual fitness tracking social networks. First, we analyze whether FTSNs leak sufficient distance metadata through their APIs to enable our attack. Table 3 shows that the EPZ implementations of 3 and 5 fitness tracking social networks are vulnerable to our attacks in an inner and total distance scenario (Section 4.3), respectively. Relive is the only network that is never vulnerable to our attack, since it enforces EPZs by truncating activities to only the track outside the EPZ when uploading. However, this truncation significantly reduces usability (Section 7).

Next, we examine the efficacy of our attack with the privacy metrics from Section 6.2 on the collected data set from Section 5 against all radii in the studied radii set. The results for the inner distance and total distance scenario are shown in Tables 4 and 5 (Appendix C) respectively, and visualized altogether in Figure 6. Note that, except for success rate, which is computed as a percentage of binary success across all EPZs, we report the median across all EPZs of the per-EPZ privacy metric values.

In the inner distance scenario, we achieve a success rate of up to 85% for EPZs with a radius of 200 m, the most popular option across Strava users (Figure 13). We notice a decrease in efficacy of the attack as the EPZ radius increases, as depicted in Figure 6. Nevertheless, even for the largest radius (1600 m), we still successfully deanonymize 39% of protected locations. We achieve almost identical success rates for the total distance scenario.

For larger radii, the number of nodes inside the EPZ (i.e., the candidate protected locations), as well as the number of nodes at roughly the same distance from the entry gates of the EPZ increases. This leads to more _confusion_ between candidate locations in our LAD regression from Section 4.3.4, since more candidate nodes have similar distances. Increasing the radius, therefore, yields predictions with increased accuracy (i.e., larger confidence intervals), which in turn, enlarges the uncertainty region from the adversary’s perspective. Reduction of the _𝑘_ -anonymity set, on the other hand, increases because the growth of the accuracy is smaller than the growth of the number of candidate nodes. The median accuracy amounts to 10 nodes for the inner distance scenario and a 200 m

100 100
80 Success Rate (%) 96
60 92
40 88
20 84 Reduction (%)
0 80
320 800
240 Correctness (m) 600
160 400
80 200 Uncertainty Region (m 2 )
0 0
100
32 Accuracy 80 Degree of Anonymity (%)
24 60
16 40
8 20
0 0
2.4 2.4 Spatial Certainty
1.8 1.8
1.2 1.2
0.6 Certainty 0.6
0.0 0.0
EPZ Radius (m) EPZ Radius (m)
Inner distance Total distance
200 400 600 8001000120014001600 200 400 600 8001000120014001600

**Figure 6: Privacy metrics from Section 6.2 for the predictions resulting from our attack, representing the attack’s efficacy.**

radius, resulting in a 92% reduction of the _𝑘_ -anonymity set and an uncertainty area of 188 _𝑚_<sup>2</sup> . In the total distance scenario, we have fewer ‘suitable’ activity endpoints compared to the inner distance scenario: as mentioned in Section 4.3.3, we filter out the activity endpoints where the user did not follow the shortest path. This reduction in suitable endpoints negatively impacts the performance of the attack, as we will discuss in Section 6.4. For smaller radii, the total distance attack has a slightly higher accuracy, resulting in smaller reduction and larger uncertainty areas compared to the inner distance attack.

The confusion also negatively impacts the correctness of our prediction, since the probability of predicting nodes other than the ground truth increases. Moreover, the larger the radius, the less probable it is that a user takes the shortest path inside the EPZ, violating Assumption A4. To a lesser extent, the number of activities our model can use for its prediction decreases as larger radii are (nearly) enveloping entire activities. We achieve a median correctness of 15m for the inner distance scenario and a 200 m radius vs. 29m in the total distance scenario.

An adversary will have similar certainty for both distance scenarios, steadily increasing with increasing radius (which also increases the number of nodes), meaning that an attacker is less confident in selecting one solution _𝑣𝑝_ ∈ _𝑉𝑝𝑟𝑒𝑑_ . However, using spatial certainty as a metric, an attacker is more confident in (geographically) pinpointing one location in the inner distance scenario than the total distance scenario. For the most popular radius, our attack achieves a median spatial certainty of almost 0, meaning that we are able to pinpoint a single location. Finally, the Degree of Anonymity remains almost constant with increasing radius for both attack scenarios, since the certainty of the attacker increases linearly with the logarithm of the _𝑘_ -anonymity set size.

## Slide 10

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert

_Comparison With Prior Work._ Our attack achieves a success rate comparable to that of Hassan et al.’s main attack which uses circle fitting [24]. Hassan et al. report a global 84% success rate, and while their results are not fully broken down by radius, they report a 44% success rate for 1 km radii. We achieve a success rate of up to 85% (for 200 m radii) and a 55% success rate for 1 km radii. However, our attack works for a harder-to-break EPZ implementation that includes spatial cloaking, for which Hassan et al.’s main attack does not work, and we use a lower error threshold ( _𝜏𝑒_ = 22 _._ 95 m for us vs. 50 m for Hassan et al.). In addition, Hassan et al. proposed spatial cloaking as a countermeasure, and evaluated an alternative interpolation attack on EPZs to which spatial cloaking has been applied [24, Section 6.4]. Their attack relies only on route direction, resulting in a success rate of at most 45% (for a radius of 200 m). Our attack using regression across distance metadata performs up to two times better (for similar radii) than Hassan et al.’s alternative attack, with our attack having up to 85% success, again at a stricter error threshold. Therefore, we effectively circumvent the countermeasure of Hassan et al. adopted by major FTSNs.

Mink et al. [35] found that human users can infer up to 68% of all sensitive locations in their data set, but again for the original EPZ implementation without spatial cloaking and with a laxer error threshold. In comparison, our (automated) attack achieves a higher success rate and works on EPZs with spatial cloaking by leveraging topological information. While Mink et al. propose that humans may also use topological information for visual inference, we conjecture that the need to visually trace the precise distances travelled within the EPZ will make the visual inference task much less successful at deanonymizing spatially cloaked protected locations than our LAD regression.

## **6.4 Sensitivity Analysis**

In order to better understand the conditions in which our attack performs better or worse, and eventually develop more effective countermeasures, we now analyze attack performance when different factors are varied.

_6.4.1 Suitable Activity Endpoints._ We first analyze whether more activities and endpoints lead to better performance. As the number of activity endpoints (i.e., observations for LAD regression in Section 4.3.4) increases, the variance of the difference between observed and theoretical distances for our prediction will decrease. More activities contribute to a slightly higher success rate for predictions, independent of the EPZ radius, as Figure 7 indicates.

_6.4.2 Entry Gates._ An increased number of entry gates yields a slightly higher success rate for smaller radii, as can be seen in Figure 7. The effect for larger radii is nullified by users not taking the shortest path. In fact, the geographic distribution of entry gates has a higher impact on the success rate of our predictions than the number of entry gates.

_6.4.3 Blind Spot Angle._ We present the _maximum blind spot angle_ as a metric to measure this geographic distribution and define it as the maximum angle between entry gates relative to the center of the EPZ. Smaller blind spot angles provide more diversified observations for the LAD regression in Section 4.3.4 than observations

within one entry gate. These diverse observations increase the difference between theoretical shortest path distances and observed distances of erroneous nodes, making it less likely that the LAD regression selects the wrong locations. This explains the higher success rate, as can be seen in Figure 7.

_6.4.4 Density of Road Network._ As the EPZ radius increases, we observe an increasing negative effect of increased street density (expressed as meters of road per square kilometer) on the success rate of our predictions, as Figure 7 shows. As the density increases, so does the number of nodes with the same distance from the entry gates of the EPZ. This increased number of candidate nodes causes confusion in the LAD regression, resulting in larger confidence intervals and the prediction of incorrect nodes which, in turn, has a negative influence on the success rate. Moreover, a denser road network gives the user more routes to take that are not the shortest path, again violating Assumption A4.

As one might expect for a distance-based attack, performance primarily depends on geographic factors. Increased geographic diversity in entry gates reduces confusion between candidate locations, particularly with sparser street grids and with smaller maximum blind spots. An increased number of activities is, therefore, only useful for our predictions if they introduce additional geographic disparity. Otherwise, their effect on the performance of our attack is moderate.

## **7 COUNTERMEASURES**

Our evaluation shows that identifying protected locations remains feasible with current EPZ implementations. While other privacy defenses exist, users tend to use these in combination with EPZs, and users still find EPZs efficient [35]. In this section, we therefore develop and evaluate potential countermeasures that support the continued use of EPZs by making EPZs more resilient against our attack. We evaluate our countermeasures on the inner distance scenario of an EPZ with a radius of 400 meters. This inner distance scenario on a small radius is favorable from the adversary’s viewpoint, yet accounts for the majority of EPZs in our data set as discussed in Section 5.2. We also discuss the usability and privacy implications and trade-offs of our countermeasures.

## **7.1 Distance-Focused Countermeasures**

Our attack primarily relies on the availability of the distance covered within the EPZ. Countermeasures could seek to obfuscate these distances, in order to increase the error in our regression. This also has the effect of altering the total traveled distance.

_C1 – Generalization._ By reducing the precision of any reported distance shown to a non-owner user [44, 45, 53], the adversary would be unable to reliably determine the distance between the actual and cloaked start/finish points (whether inner or total distances). This reduces the precision of the last step of Algorithm 2 (Section 4.3.4), in which we search the point where the theoretical shortest path distances best correspond to the actually observed distances. We implement generalization by rounding distances to the nearest multiple of a certain integer value. In Figure 8, we evaluate the performance of our attack given different roundings of the inner distance; note that the maximum perturbation is half of

## Slide 11

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks

90%
75%
60%
45%
30%
10 1 10 2 4 8 12 16 60 120 180 240 300 360 10000 20000 30000
Suitable Activity Endpoints Entry Gates Blindspot Angle ( ) Street Density (m/km 2 )
EPZ radius (m)
400 800 1200
Success Rate

**Figure 7: Logistic regression of the independent variable ‘success’ of our attack for the predictor variables selected in our sensitivity analysis, across three EPZ radii.**

100 100
80 99 Reduction (%)
60 98
40 Success Rate (%) 97
20 96
0 95
300
600
240 Correctness (m) 450 Uncertainty Region (m 2 )
180
120 300
60 150
0 0
3024 Accuracy 3024
18 18
12 12
6 6 Degree of Anonymity (%)
0 0
2.7 0.7
2.4 Certainty 0.6 Spatial Certainty
2.1 0.5
1.8
1.5 0.4
1.2 0.3
Maximum perturbation (m) Maximum perturbation (m)
Baseline (no defense) C2. Noisy distances
C1. Generalization C3. Shifting distances
2550 100 150 200 250 500 2550 100 150 200 250 500

**Figure 8: Impact of countermeasures C1-C3**<sup>6</sup> **on the privacy metrics for our predictions and therefore on the efficacy of our attack, for the inner distance scenario on an EPZ with a 400 m radius. Full numerical results are presented in Table 6 (Appendix C).**

the rounding distance. We find that the success rate fully breaks down after a rounding of around 500 meters, although even small roundings already largely reduce this success rate. Argyros et al. [6] similarly found that attack performance is inversely proportional to the magnitude of the applied rounding. As the rounding distance increases, the uncertainty of the adversary (wrongly) decreases: multiple observations get mapped onto the same generalized value leading to less confusion in the last step of Algorithm 2. This makes the adversary more certain of their false predictions.

_C2 – Noisy distances._ This countermeasure applies random noise to the reported distance, instead of rounding it. This adds more uncertainty to the predictions of the adversary, resulting in bigger confidence intervals and uncertainty regions, as depicted in Figure 8.

6Note that metrics for C2 and C3 strongly overlap.

However, multiple activities from the same entry gate would result in these random shifts being averaged out, causing the ground truth to be present in the confidence interval. With the ground truth still present in the confidence interval, we observe no change in the success rate.

_C3 – Shifting distances._ The reported endpoints are shifted by a fixed or random distance, while retaining the originally traveled distance as the total distance. However, similar to the noisy distances countermeasure, these random shifts may be averaged out across activities. In Figure 8, we see an increased uncertainty region of the adversary compared to the baseline. However, since the success rate has not changed, _𝑘_ -anonymity has not been restored.

_C4 – Truncation._ A more invasive countermeasure consists of eliminating the track portions lying within the EPZ entirely, by not including them in the reported total and accumulated distances, or even hiding the full track. This would effectively thwart our attack, as we can no longer infer where on the street grid inside the EPZ the activity may have started and ended; only a random guess among all possible protected locations remains possible.

The main disadvantage of altering the reported distances lies in their negative usability impact. Whereas in other location-based services such as check-in apps, an error of several hundreds of meters may be acceptable [6], this may be less the case for fitness social networks. Part of the attraction of these networks comes from the gamification of exercise activities [7], such as achievements for covering certain distance goals or being able to compare across small performance differences (in the order of seconds) [14], which require high detail in activity data. Aggressive rounding of distances would result in losing the desired precision at which the distance and pace are measured, possibly leading to overestimated achievements. Removing the track portions inside the EPZ and shortening the track distance is, therefore, also unattractive: it would result in underestimating the achieved distance.

## **7.2 EPZ-Focused Countermeasures**

Countermeasures could target the EPZ to decrease (the utility of) available data or the identification of the EPZ (Algorithm 1).

_C5 – Increasing EPZ radii._ An obvious countermeasure is increasing the EPZ radius. Our evaluation in Section 6.3 confirms that, for circular EPZs, the attack performance decreases when the EPZ radius increases. However, this severely reduces usability, particularly for shorter activities, as they may be entirely covered by the

## Slide 12

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert

EPZ. This might also be why larger EPZ radii are less popular than smaller radii (as seen in our data set in Section 5.2).

_C6 – Complex EPZs/cloaking._ Beyond circular EPZs with a small set of possible radii, different EPZ layouts could be implemented: circles with any radius or even any shape. Hassan et al. [24] proposed a similar strategy by hiding a (small) track portion of random<sup>7</sup> length beyond the EPZ border (“Fuzz EPZ Intersection Points”). Alternatively, the concept of a ‘zone’ could be discarded, and instead a fixed or variable distance from the start and finish points could be cloaked, as Strava has recently implemented [32]. For our attack, this only affects the phase of identifying EPZs, as this step will be less reliable due to the noise applied to the cloaked endpoints. Afterwards, the countermeasure has no effect on our location prediction algorithm: the inner/total distances and endpoints remain available, and allow for regression.

More complex zones require more complex identification algorithms, beyond the least squares fit for circular EPZs (Algorithm 1). These algorithms may be less accurate at identifying EPZs. More complex zones may also make the removal of deviating activities (Section 4.3.3) less effective, as the threshold for becoming an outlier becomes less likely to be met. However, as stated in Section 4.2, our attack still works with imprecise EPZ identification. Countermeasures that make EPZ discovery harder, therefore, cannot fully thwart our attack. Crucially, these countermeasures do not affect the availability nor accuracy of the reported distances. Any increase in the search space due to a less compact EPZ will reduce the attack performance by increasing the likelihood that an erroneous location is predicted, and it will make the attack more computationally expensive.

Finally, a number of apparent countermeasures may seem effective at first, but can potentially _improve_ the efficacy of our attack. Regeneration of an EPZ recomputes the endpoints for every (future) activity, and may, therefore, generate additional entry gates, as the edge of the EPZ has now shifted. This yields additional and more diverse data, which could improve the correctness of our attack, since our evaluation in Section 6.4 shows that correctness tends to decrease when there are more entry gates and activities. Next, smoothing the track by map matching nodes to the road network would remove any (small) deviations that cause the actual traveled distance to not match the theoretical shortest path exactly, and would, therefore, make the LAD regression step more accurate.

In summary, distance-based countermeasures and in particular generalization are the most effective, but can severely reduce usability. Countermeasures that target EPZ discovery are less invasive, but only partially prevent our attack.

## **8 RELATED WORK**

Two recent works have analyzed vulnerabilities in previous implementations of EPZs where no spatial cloaking was applied and the center of the EPZ was therefore the protected location. In 2018, Hassan et al. [24] were able to infer EPZs and their protected locations by fitting circles between pairs of endpoints. They identified 84% of 432,022 athletes across 2.3 million EPZ-enabled Strava activities. In 2022, Mink et al. [35] showed that users could visually

identify up to 68% of protected locations when asked to draw the EPZ between activity endpoints overlaid on a map and pinpoint the protected location. Hassan et al. [24] proposed several countermeasures, which were implemented by some fitness tracking networks. Crucially, both works therefore only prove the vulnerability of an EPZ implementation that is by now arguably outdated. In contrast to both works, our attack breaks the current state-of-the-art EPZs, i.e., those when spatial cloaking is present, with a comparable or higher success rate than the prior work, on a harder-to-break EPZ implementation. We also analyze in depth to which factors of privacy zones our attack is sensitive.

Other work has explored other privacy concerns in sharing location data on fitness tracking social networks. Beyond privacy zones, Meteriz et al. [34] found that elevation profiles could be sufficient to recover a location at borough- or city-level, even if the location data is not shared. They require prior knowledge of potentially visited locations, which are predicted at very low granularity, unlike our attack. Alqhatani and Lipfore [2], Zimmer et al. [58], Gabriele and Chiasson [20], Couture [14], and Mink et al. [35] described how users are somewhat aware of the privacy implications of sharing location data on fitness tracking social networks, but that this awareness may be insufficient. They also found that users differ in their sensitivity to having sensitive locations publicly available, correlating with concerns on personal space and physical safety. Mink et al. [35] found that users consider EPZs an effective privacy mechanism, but that these users would mostly use EPZs together with other privacy mechanisms.

Beyond fitness services, prior work has evaluated the feasibility of de-anonymizing implementations for location proximity, where the distance to nearby users is shown instead of their actual location. Li et al. [29] developed attacks for three popular location proximity services, accurate to up to 25 meters. Argyros et al. [6, 40] showed that major location proximity services remained vulnerable to location inference attacks, despite existing countermeasures. These attacks were sufficiently performant to enable real-time tracking. These two studies proposed some form of spatial cloaking [23] as an effective countermeasure. Qin et al. [41] and Zhao et al. [57] showed for 4 and 29 apps respectively that revealed distances enable trilateration attacks.

On the side of defenses, Gruteser and Grunwald [23] proposed spatial and temporal cloaking, where an error is introduced to the location information, e.g., by decreasing resolution or applying random noise. Cheng et al. [13] evaluated the trade-off between such cloaking and the quality of the provided service, and propose imprecise queries across cloaked locations to improve this trade-off. Ardagna et al. [5] concretely defined obfuscation techniques on circular zones (compare to circular EPZs). Duckham and Kulik [17] formalized obfuscation as a means to achieve location privacy, implemented through precision reduction (similar to cloaking). Andrés et al. [3] formally introduced geo-indistinguishability, where a user reveals a sufficiently approximate location to receive a desired service, instead of their exact location. In this and follow-up work [9, 11, 12], they proposed several techniques for achieving this property.

7A fixed shift would be equivalent to increasing the EPZ radius.

## Slide 13

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks

## **9 ETHICS AND RESPONSIBLE DISCLOSURE**

We disclosed this research project to our university’s privacy and ethics board before we collected any data or ran any experiments. Our project was formally approved, and we implemented all recommendations regarding pseudonymization of user and activity IDs, and data retention on secure internal network storage servers.

During the course of this project, we discovered several fundamental problems in how fitness tracking social networks implement EPZs. We disclosed our findings to the affected parties from Table 3 by sending them a draft of this manuscript and by formulating recommendations for improving the privacy of their users.

## **10 CONCLUSION**

Major fitness tracking social networks have introduced endpoint privacy zones as a tool to protect sensitive locations from being revealed to malicious actors. However, despite the usage of spatial cloaking, we show that these protected locations can still be discovered reliably. Our attack leverages the reported distances traveled within the EPZ, as well as the layout of the street grid to deanonymize protected locations with a success rate of up to 85%. While distance-based countermeasures such as generalization can be effective at thwarting our attack, they can also severely reduce usability. Networks must, therefore, carefully consider which functionality they provide while guaranteeing user privacy.

## **11 ADDENDUM: SPATIAL CERTAINTY**

We design a new metric to measure _spatial certainty_ , which represents the geographical closeness of predictions. For example, consider two situations (a) and (b), depicted in Figure 9, where an attacker predicts four locations inside an EPZ with uniform probability. Whereas the predictions in (a) are geographically dispersed, the predictions in (b) are geographically concentrated.

Shokri [48] defined certainty as the Shannon entropy [46] of the estimate probability distribution _𝑃𝑟_<sup>�</sup> ( _𝑣_ | _𝑎_ ). This entropy shows how concentrated _𝑃𝑟_<sup>�</sup> ( _𝑣_ | _𝑎_ ) is and, thus, how easy it is to pinpoint a single outcome _𝑣𝑝_ ∈ _𝑉𝑝𝑟𝑒𝑑_ . Since this distribution _𝑃𝑟_<sup>�</sup> ( _𝑣_ | _𝑎_ ) is the

**(a) Geographically dispersed predic(b) Geographically concentrated pretions of an adversary. dictions of an adversary. (certainty=1.39, spatial certainty=1.39) (certainty=1.39, spatial certainty=0.0)**

**Figure 9: Geographical plot of predictions of an adversary. Each node** _𝑣_ ∈ _𝑉_ **, displayed in red, is a potential protected location. Each actual predicted node** _𝑣𝑝_ ∈ _𝑉𝑝𝑟𝑒𝑑_ **is displayed in blue.**

same in (a) as in (b), it will result in the same value for certainty. However, the certainty value does not give a notion of the spatial concentration of predictions.

By increasing the chaining resolution (i.e., reducing the chaining distance _𝑑𝑐ℎ𝑎𝑖𝑛_ , as explained in Section 4.3), the number of possible protected nodes _𝑣_ ∈ _𝑉_ increases. This will make it harder for an attacker to pinpoint a single solution _𝑣𝑝_ ∈ _𝑉𝑝𝑟𝑒𝑑_ . However, we only claim to predict a location with _𝜏𝑒_ precision. Therefore, we should consider neighborhoods of nodes within _𝜏𝑒_ when determining if a prediction is sufficiently close to the protected location.

We additionally define spatial certainty as Karlstrom and Ceccato’s entropy [26]. Instead of using the logarithm of the probability of a single node _𝑣_ as the surprisal term in the entropy formula, we use the logarithm of the sum of all neighboring nodes _𝑣 𝑗_ probabilities of _𝑣_ including _𝑣_ itself:

A node _𝑣 𝑗_ is considered a neighbor of _𝑣_ if the Euclidean distance between both nodes is less than or equal to _𝜏𝑒_ :

## **ACKNOWLEDGMENTS**

We thank the anonymous reviewers for their valuable and constructive feedback, as well as the Security Analytics SIG at DistriNet. This research is partially funded by the Research Fund KU Leuven, and by the Flemish Research Programme Cybersecurity. Victor Le Pochat holds a PhD Fellowship of the Research Foundation Flanders - FWO (11A3421N). Map tiles by Stamen Design, under CC BY 3.0. Map data from OpenStreetMap, under ODbL.

## **REFERENCES**

- [1] Adidas. 2021. adidas Runtastic: adidas Running & adidas Training apps. Retrieved Sept. 21, 2021 from https://www.runtastic.com/.

- [2] Abdulmajeed Alqhatani and Heather Richter Lipford. 2019. “There is nothing that I need to keep secret”: Sharing Practices and Concerns of Wearable Fitness Data. In _15th Symposium on Usable Privacy and Security_ (SOUPS ’19), 421–434.

- [3] Miguel E. Andrés, Nicolás E. Bordenabe, Konstantinos Chatzikokolakis, and Catuscia Palamidessi. 2013. Geo-Indistinguishability: Differential Privacy for Location-Based Systems. In _2013 ACM SIGSAC Conference on Computer and Communications Security_ (CCS ’13), 901–914. doi: 10.1145/2508859.2516735.

- [4] Carmen Ang. 2020. The Growth of Home Fitness Apps. Visual Capitalist. (Sept. 10, 2020). https://www.visualcapitalist.com/the- growth- of - home -fitness-apps-2020/.

- [5] C. A. Ardagna, M. Cremonini, E. Damiani, S. De Capitani di Vimercati, and P. Samarati. 2007. Location Privacy Protection Through Obfuscation-Based Techniques. In _IFIP Annual Conference on Data and Applications Security and Privacy_ , 47–60. doi: 10.1007/978-3-540-73538-0_4.

- [6] George Argyros, Theofilos Petsios, Suphannee Sivakorn, Angelos D. Keromytis, and Jason Polakis. 2017. Evaluating the Privacy Guarantees of Location Proximity Services. _ACM Transactions on Privacy and Security_ , 19, 4, Article 12, (Feb. 2017), 31 pages. doi: 10.1145/3007209.

- [7] Paul Barratt. 2017. Healthy competition: A qualitative study investigating persuasive technologies and the gamification of cycling. _Health & Place_ , 46, (July 2017), 328–336. doi: 10.1016/j.healthplace.2016.09.009.

- [8] Geoff Boeing. 2017. OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks. _Computers, Environment and Urban Systems_ , 65, 126–139. doi: 10.1016/j.compenvurbsys.2017.05.004.

## Slide 14

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert

- [9] Nicolás E. Bordenabe, Konstantinos Chatzikokolakis, and Catuscia Palamidessi. 2014. Optimal Geo-Indistinguishable Mechanisms for Location Privacy. In _2014 ACM SIGSAC Conference on Computer and Communications Security_ (CCS ’14), 251–262. doi: 10.1145/2660267.2660345.

- [10] Kaya Burgess. 2018. Thieves ‘followed rider on his Strava app’ to make off with £12,500 in bikes. _The Times_ , (Sept. 22, 2018). https://www.thetimes.co.uk/articl e/thieves-followed-rider-on-his-strava-app-to-make-off-with-12-500-in-bi kes-xqjrlgj0f.

- [11] Konstantinos Chatzikokolakis, Catuscia Palamidessi, and Marco Stronati. 2014. A Predictive Differentially-Private Mechanism for Mobility Traces. In _Privacy Enhancing Technologies_ , 21–41. doi: 10.1007/978-3-319-08506-7_2.

- [12] Konstantinos Chatzikokolakis, Catuscia Palamidessi, and Marco Stronati. 2015. Constructing elastic distinguishability metrics for location privacy. _Proceedings on Privacy Enhancing Technologies_ , 2015, 2, 156–170. doi: 10.1515/popets-20150023.

- [13] Reynold Cheng, Yu Zhang, Elisa Bertino, and Sunil Prabhakar. 2006. Preserving User Location Privacy in Mobile Data Management Infrastructures. In _Privacy Enhancing Technologies_ , 393–412. doi: 10.1007/11957454_23.

- [14] Jesse Couture. 2021. Reflections from the ’Strava-sphere’: Kudos, community, and (self-)surveillance on a social network for athletes. _Qualitative Research in Sport, Exercise and Health_ , 13, 1, 184–200. doi: 10.1080/2159676X.2020.1836514.

- [15] Claudia Díaz, Stefaan Seys, Joris Claessens, and Bart Preneel. 2003. Towards Measuring Anonymity. In _Privacy Enhancing Technologies_ . Springer Berlin Heidelberg, 54–68. doi: 10.1007/3-540-36467-6_5.

- [16] E. W. Dijkstra. 1959. A Note on Two Problems in Connexion with Graphs. _Numerische Mathematik_ , 1, 1, (Dec. 1959), 269–271. doi: 10.1007/BF01386390.

- [17] Matt Duckham and Lars Kulik. 2005. A Formal Model of Obfuscation and Negotiation for Location Privacy. In _International Conference on Pervasive Computing_ , 152–170. doi: 10.1007/11428572_10.

- [18] B. Efron. 1979. Bootstrap Methods: Another Look at the Jackknife. _The Annals of Statistics_ , 7, 1, 1–26. doi: 10.1214/aos/1176344552.

- [19] Martin Ester, Hans-Peter Kriegel, Jörg Sander, and Xiaowei Xu. 1996. A DensityBased Algorithm for Discovering Clusters in Large Spatial Databases with Noise. In _2nd International Conference on Knowledge Discovery and Data Mining_ (KDD’96). AAAI Press, 226–231.

- [20] Sandra Gabriele and Sonia Chiasson. 2020. Understanding Fitness Tracker Users’ Security and Privacy Knowledge, Attitudes and Behaviours. In _2020 CHI Conference on Human Factors in Computing Systems_ (CHI ’20). doi: 10.1145/331 3831.3376651.

- [21] Garmin. 2021. Garmin Connect | Free Online Fitness Community. Retrieved Sept. 21, 2021 from https://connect.garmin.com/.

- [22] Ralph Gross, Alessandro Acquisti, and H. John Heinz. 2005. Information revelation and privacy in online social networks. In _2005 ACM workshop on Privacy in the electronic society_ (WPES ’05). doi: 10.1145/1102199.1102214.

- [23] Marco Gruteser and Dirk Grunwald. 2003. Anonymous Usage of LocationBased Services Through Spatial and Temporal Cloaking. In _1st international conference on Mobile systems, applications and services_ (MobiSys ’03). doi: 10.1 145/1066116.1189037.

- [24] Wajih Ul Hassan, Saad Hussain, and Adam Bates. 2018. Analysis of Privacy Protections in Fitness Tracking Social Networks -or- You can run, but can you hide? In _27th USENIX Security Symposium_ , 497–512.

- [25] Alex Hern. 2018. Fitness tracking app Strava gives away location of secret US army bases. _The Guardian_ , (Jan. 28, 2018). https://www.theguardian.com/worl d/2018/jan/28/fitness-tracking-app-gives-away-location-of-secret-us-armybases.

- [26] Anders Karlström and Vânia Ceccato. 2002. A new information theoretical measure of global and local spatial association. _Jahrbuch fur Regionalwissenschaft_ , 22, 1, 13–40.

- [27] Komoot. 2021. Komoot | Find, plan and share your adventures. Retrieved Sept. 21, 2021 from https://www.komoot.com/.

- [28] Komoot. 2020. Privacy Zones. (Aug. 18, 2020). https://support.komoot.com/hc /en-us/articles/360046595312.

- [29] Muyuan Li, Haojin Zhu, Zhaoyu Gao, Si Chen, Le Yu, Shangqian Hu, and Kui Ren. 2014. All Your Location Are Belong to Us: Breaking Mobile Social Networks for Automated User Location Tracking. In _15th ACM International Symposium on Mobile Ad Hoc Networking and Computing_ (MobiHoc ’14), 43–52. doi: 10.1145/2632951.2632953.

- [30] J. MacQueen. 1967. Some methods for classification and analysis of multivariate observations. In _5th Berkeley Symposium on Mathematical Statistics and Probability_ . Vol. 1, 281–297.

- [31] Map My Tracks. 2021. Map My Tracks - your active life in one app. Retrieved Sept. 21, 2021 from https://www.mapmytracks.com/.

- [32] Meg. 2021. Edit Map Visibility. Strava Support. (Aug. 18, 2021). https://support .strava.com/hc/en-us/articles/115000173384.

- [33] Meg. 2020. Your Privacy Defaults when you Create a Strava Account. Strava Support. (Oct. 13, 2020). https://support.strava.com/hc/en-us/articles/36003475 8331.

- [34] Ülkü Meteriz, Necip Fazıl Yıldıran, Joongheon Kim, and David Mohaisen. 2020. Understanding the Potential Risks of Sharing Elevation Information on Fitness Applications. In _40th IEEE International Conference on Distributed Computing Systems_ (ICDCS ’20), 464–473. doi: 10.1109/ICDCS47774.2020.00063.

- [35] Jaron Mink, Amanda Rose Yuile, Uma Pal, Adam J. Aviv, and Adam Bates. 2022. Users Can Deduce Sensitive Locations Protected by Privacy Zones on Fitness Tracking Apps. In _2022 ACM CHI Conference on Human Factors in Computing Systems_ (CHI ’22). doi: 10.1145/3491102.3502136.

- [36] Arvind Narayanan and Vitaly Shmatikov. 2008. Robust De-anonymization of Large Sparse Datasets. In _2008 IEEE Symposium on Security and Privacy_ (SP ’08). doi: 10.1109/sp.2008.33.

- [37] Nick. 2019. Automatic privacy zone detection. Map My Tracks. (Jan. 28, 2019). https://www.mapmytracks.com/blog/entry/automatic-privacy-zone-detectio n.

- [38] Nike. 2021. Nike Run Club App. Nike.com. Retrieved Sept. 21, 2021 from https: //www.nike.com/nrc-app.

- [39] Olivia Nuzzi. 2020. What It’s Like to Get Doxed for Taking a Bike Ride. _Intelligencer_ , (June 8, 2020). https://nymag.com/intelligencer/2020/06/what-its-like-t o-get-doxed-for-taking-a-bike-ride.html.

- [40] Iasonas Polakis, George Argyros, Theofilos Petsios, Suphannee Sivakorn, and Angelos D. Keromytis. 2015. Where’s Wally?: Precise User Discovery Attacks in Location Proximity Services. In _22nd ACM SIGSAC Conference on Computer and Communications Security_ (CCS ’15). doi: 10.1145/2810103.2813605.

- [41] Guojun Qin, Constantinos Patsakis, and Mélanie Bouroche. 2014. Playing Hide and Seek with Mobile Dating Applications. In _29th IFIP International Information Security Conference_ , 185–196. doi: 10.1007/978-3-642-55415-5_15.

- [42] Relive. 2021. Relive | Run, Ride, & more. Retrieved Sept. 21, 2021 from https: //www.relive.cc/.

- [43] Ride with GPS. 2021. Ride with GPS | Bike Route Planner and Cycling Navigation App. Retrieved Sept. 21, 2021 from https://ridewithgps.com/.

- [44] Pierangela Samarati. 2001. Protecting respondents identities in microdata release. _IEEE Transactions on Knowledge and Data Engineering_ , 13, 6, 1010–1027. doi: 10.1109/69.971193.

- [45] Pierangela Samarati and Latanya Sweeney. 1998. Generalizing Data to Provide Anonymity When Disclosing Information (Abstract). In _17th ACM SIGACTSIGMOD-SIGART Symposium on Principles of Database Systems_ (PODS ’98), 188. doi: 10.1145/275487.275508.

- [46] C. E. Shannon. 1948. A Mathematical Theory of Communication. _Bell System Technical Journal_ , 27, 3, (July 1948), 379–423. doi: 10.1002/j.1538-7305.1948.tb0 1338.x.

- [47] Ax Sharma. 2020. Strava app shows your info to nearby users unless this setting is disabled. _BleepingComputer_ , (Sept. 21, 2020). https://www.bleepingcomputer .com/news/security/strava-app-shows-your-info-to-nearby-users-unless-th is-setting-is-disabled/.

- [48] Reza Shokri, George Theodorakopoulos, Jean-Yves Le Boudec, and Jean-Pierre Hubaux. 2011. Quantifying Location Privacy. In _2011 IEEE Symposium on Security and Privacy_ (SP ’11). doi: 10.1109/sp.2011.18.

- [49] Software Freedom Conservancy. 2021. Selenium WebDriver. https://www.sele nium.dev/documentation/webdriver/.

- [50] Strava. 2021. Strava | Run and Cycling Tracking on the Social Network for Athletes. Retrieved Sept. 21, 2021 from https://www.strava.com.

- [51] Strava. 2020. Strava releases 2020 Year In Sport Data Report. (Dec. 16, 2020). https://blog.strava.com/press/yis2020/.

- [52] 2022. Strava’s Global Community Continues Strong Growth Surpassing 100M Registered Athletes on the Platform. Strava. (May 24, 2022). https://blog.strava .com/press/100million/.

- [53] Latanya Sweeney. 2002. Achieving k-anonymity privacy protection using generalization and suppression. _International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems_ , 10, 05, (Oct. 2002), 571–588. doi: 10.1142/s02184885 0200165x.

- [54] Emily Tseng, Rosanna Bellini, Nora McDonald, Matan Danos, Rachel Greenstadt, Damon McCoy, Nicola Dell, and Thomas Ristenpart. 2020. The Tools and Tactics Used in Intimate Partner Surveillance: An Analysis of Online Infidelity Forums. In _29th USENIX Security Symposium_ (USENIX Security ’20), 1893–1909.

- [55] Under Armour. 2021. MapMyRun. Retrieved Sept. 21, 2021 from https://www .mapmyrun.com/.

- [56] Delanie Woodlock. 2016. The Abuse of Technology in Domestic Violence and Stalking. _Violence Against Women_ , 23, 5, (July 2016), 584–602. doi: 10.1177/107 7801216646277.

- [57] Fanghua Zhao, Linan Gao, Yang Zhang, Zeyu Wang, Bo Wang, and Shanqing Guo. 2018. You Are Where You App: An Assessment on Location Privacy of Social Applications. In _2018 IEEE 29th International Symposium on Software Reliability Engineering_ (ISSRE ’18), 236–247. doi: 10.1109/ISSRE.2018.00033.

- [58] Michael Zimmer, Priya Kumar, Jessica Vitak, Yuting Liao, and Katie Chamberlain Kritikos. 2020. ‘There’s nothing really they can do with this information’: unpacking how users manage privacy boundaries for personal fitness information. _Information, Communication & Society_ , 23, 7, 1020–1037. doi: 10.1080/136 9118X.2018.1543442.

## Slide 15

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks

## **A ABSOLUTE MAP MATCHING ERROR**

60
50
40
30
Elbow point: 22.95m
20
10
0
Cumulative % of users
0% 20% 40% 60% 80% 92%100%
Map matching error (m)

**Figure 10: Distribution of the absolute map matching error across our 1.4 million Strava activities. We select the elbow point as our threshold for successful prediction.**

A user may start and/or finish at a point away from the street grid (e.g., on private property), meaning that the uncloaked endpoints may be far away from our streetside ground-truth location. We, therefore, measure the absolute map matching error (i.e., the distance between the ground truth and the centroid of uncloaked endpoints that is used to construct the ground truth) and show its distribution in Figure 10. This additional distance leads to less precise predictions from our model, with the possibility of predicting ‘overshoot’ locations on the road network but away from our ground truth. In order to cover these corner cases, we define our prediction to be ‘successful’ (binary value) if the error of its location to the ground truth is less than an error threshold _𝜏𝑒_ . We empirically select _𝜏𝑒_ as the distance of the elbow point (22.95m) of the absolute map matching error distribution. 92% of users in our data set have a map matching error smaller than this distance.

## **B DATA SET CHARACTERISTICS**

100%
80%
60%
40%
20%
0%
10 0 10 1 10 2 10 3
Number of activities
Figure 11: Cumulative distribution of number of activities
per user over our data set of 4,000 Strava users.
10 4
10 2
10 0
Figure 12: Geographic distribution of activity endpoints over
our data set of 4,000 Strava users.
30.0%
20.0%
10.0%
0.0%
EPZ radius (m)
Cumulative user percentage
Number of endpoints
Usage percentage
legacy 200 400 600 800 1000 1200 1400 1600

**Figure 11: Cumulative distribution of number of activities per user over our data set of 4,000 Strava users.**

**Figure 12: Geographic distribution of activity endpoints over our data set of 4,000 Strava users.**

**Figure 13: Distribution of selected EPZ radii across 461 Strava users that use the EPZ cloaking mechanism.**

## Slide 16

CCS ’22, November 7–11, 2022, Los Angeles, CA, USA

Karel Dhondt, Victor Le Pochat, Alexios Voulimeneas, Wouter Joosen, and Stijn Volckaert

## **C FULL PRIVACY METRICS RESULTS**

**Table 4: Inner distance attack privacy metrics.**

||Success Rate (%)|Correctness (m)|Accuracy|Reduction (%)|Uncertainty Region (_𝑚_<sup>2</sup>)|Certainty|Spatial Certainty|Degree of Anonymity (%)|
|---|---|---|---|---|---|---|---|---|
|Radius (m)|||||||||
|200|85.55|15.79|10|92.21|188.97|1.51|0.04|22.96|
|400|77.26|27.11|14|96.67|267.75|1.78|0.24|22.79|
|600|69.09|45.09|19|97.86|361.25|2.02|0.48|23.49|
|800|61.89|67.83|23|98.43|448.34|2.18|0.61|23.76|
|1000|54.95|97.56|27|98.71|538.75|2.32|0.71|24.42|
|1200|49.44|125.49|30|98.88|621.66|2.39|0.84|24.49|
|1400|43.83|157.49|34|98.98|704.24|2.53|0.98|25.09|
|1600|39.58|196.03|37|99.12|786.48|2.62|1.06|25.36|

**Table 5: Total distance attack privacy metrics.**

||Success Rate (%)|Correctness (m)|Accuracy|Reduction (%)|Uncertainty Region (_𝑚_<sup>2</sup>)|Certainty|Spatial Certainty|Degree of Anonymity (%)|
|---|---|---|---|---|---|---|---|---|
|Radius (m)|||||||||
|200|84.36|29.10|15|87.40|318.03|1.91|0.59|29.06|
|400|75.23|60.49|20|94.12|448.42|2.18|1.02|27.82|
|600|66.65|96.64|25|96.27|573.95|2.38|1.20|27.69|
|800|60.30|137.31|28|97.30|635.30|2.46|1.38|26.81|
|1000|54.36|180.30|30|97.93|699.12|2.54|1.52|26.69|
|1200|48.20|221.07|31|98.33|744.40|2.57|1.63|26.19|
|1400|43.33|266.53|32|98.59|787.83|2.63|1.72|26.08|
|1600|39.31|319.41|33|98.81|788.23|2.62|1.77|25.39|

**Table 6: Countermeasure privacy metrics.**

|Defence|Success Rate (%)|Correctness (m)|Accuracy|Reduction (%)|Uncertainty Region (_𝑚_<sup>2</sup>)|Certainty|Spatial Certainty|Degree of Anonymity (%)|
|---|---|---|---|---|---|---|---|---|
|Baseline (no defense)|77.26|27.11|14|96.67|267.75|1.78|0.24|22.79|
|C1 - Generalization: 50 m|76.36|29.46|13|96.64|256.72|1.59|0.34|20.26|
|C1 - Generalization: 100 m|65.15|38.89|11|96.67|222.42|1.43|0.39|18.03|
|C1 - Generalization: 200 m|43.24|56.92|10|96.72|198.94|1.28|0.37|16.22|
|C1 - Generalization: 300 m|27.58|84.80|9|96.91|184.09|1.21|0.39|15.56|
|C1 - Generalization: 400 m|15.92|118.28|9|96.97|182.07|1.21|0.40|15.33|
|C1 - Generalization: 500 m|8.58|164.74|8|97.20|170.75|1.16|0.35|14.83|
|C1 - Generalization: 1000 m|3.04|290.38|6|97.95|133.72|1.03|0.42|12.73|
|C2 - Noisy distances: 50 m|78.09|31.66|22|96.05|411.56|2.26|0.39|29.07|
|C2 - Noisy distances: 100 m|78.05|40.77|32|94.90|638.75|2.65|0.69|34.23|
|C3 - Shifting distances: 50 m|78.13|31.21|22|96.02|417.88|2.28|0.40|29.26|
|C3 - Shifting distances: 100 m|77.75|41.15|33|94.90|637.14|2.66|0.69|34.12|
