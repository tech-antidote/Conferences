---
title: "The Yandex Leak How a Russian Search Giant Uses Consumer Data"
speakers: ["Kaileigh McCrea"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Kaileigh McCrea_The Yandex Leak How a Russian Search Giant Uses Consumer Data.pdf"
pages: 75
sha256: "f192e8e4cafbfb5a5c69e78952337dc7b7d464f97f81aa32e574bacf27282f23"
text_chars: 48777
ocr_pages: 59
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:19:25Z"
---
# The Yandex Leak How a Russian Search Giant Uses Consumer Data

**Speakers:** Kaileigh McCrea  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Kaileigh McCrea_The Yandex Leak How a Russian Search Giant Uses Consumer Data.pdf` (75 pages)


## Slide 1

The Yandex Leak: How a Russian Search Giant Uses Consumer Data

Kaileigh McCrea, Privacy Engineer, Confiant

## Slide 2

#### About Me

##### Kaileigh McCrea

● Privacy Engineer at Confiant (3 yrs) ● Software Engineer (6 years)

● Cybersecurity Nerd

● Recovering Political Science major

● Twitter: @kaileighrose

2

## Slide 3

### What we’re talking about

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
yandex git sources
iby booinieRR- Wednesday January 25, 2023 at 03:48 PM
Repositories only, no data. Size 44,71 G
pied almost completely except for the anti-spam rules
Downloaded by me on 07.
magnet:?
YANDEX SERVICES SOURCE
CODE LEAK
SHORT OVERVIEW OF BREACH CONTENTS
BLEEPINGCOMPUTER
Yandex denies hack, blames source code leak on former employee
Yandex denies hack, blames source code leak on former employee
By Bill Toulas January 26, 2023 09:44 AM 1
```

## Slide 4

# Roadmap

●Background on Yandex Leak ●Dive into code: ○What data Yandex is collecting ○What Yandex is doing with that data ○Who Yandex is sharing that data with ●Conclusions and wrap up ●Q&A

4

## Slide 5

## Yandex 101

5

## Slide 6

#### Yandex 101

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Yandex 101
vy Login
2A OS OG ®@
Games Images Video Meteum Maps Mail Translate
@: 26° ee |
```

## Slide 7

#### Yandex 101

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Yandex 101
Key Businesses
Search
and Portal
Yandex Search Business
Units
Geo Services
Yandex Browser
Yandex Q
Other
E-commerce,
Mobility and
Delivery
Plus and
Entertainment
Services
Classifieds
Mobility
E-commerce
Other 020
Yandex Plus
Yandex Music
Kinopoisk
Yandex Afisha
Yandex Studio
Auto.ru
Yandex Realty
Yandex Rent
Yandex Travel
Other
Business Units
and Initiatives
Yandex SDG
Yandex Cloud
Yandex Education
Devices and Alice
Other
```

## Slide 8

#### Yandex 101

<u>AppMetrica:</u> “In-depth analytics for product and growth teams”

<u>Audiences: allows you to</u> pull data from several sources to generate your own targeted segments

<u>Crypta: “helps to identify</u> important user characteristics for advertisers”

8

## Slide 9

#### Yandex 101

9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Yandex 101
Yandex LLC
Head office in Russia: Moscow
Head office Advertising clients
16, Leo Tolstoy St., Moscow, Russia tel.:+7 495 739-37-77
119021 fax:+7 495 739-23-32
tel.:+7 495 739-70-00 adv@yandex-team.ru
fax: +7 495 739-70-70
Public relations Corporate Secretary
pr@yandex-team.ru secretary@yandex-team.ru
Investor Relations
tel.:+7 495 974-35-38
askIR@yandex-team.ru
Sustainability
sustainability@yandex-team.com
Official Telegram channel for individual investors https://t.me/yndx_forinvestors (in Russian only)
Yandex N.V.
Registered office in Amsterdam
Schiphol Boulevard 165, 1118 BG Schiphol, The
Netherlands
tel.: +31 0 20 206 6970
```

## Slide 10

## Yandex: A Drama

10

## Slide 11

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Russia © This article is more than 3 years old Advertisement
Russian internet giant grants veto
powers to Kremlin-linked body
Yandex agrees to corporate restructuring in move likely to
increase government oversight
Andrew Roth in Moscow
Mon 18 Nov 2019 06.30 ES
fi vy@
@ Arkady
daily oper
zh, the chief executive of Y aid the company would maintain control over its
s. Photograph: Mikhail Metzel,
```

## Slide 12

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Observer © This article is more than 1 year old Advertisement
Russia
Warnings raised over Russian tech giant
Yandex’s UK operation
MPs want restrictions placed on the company, known as Russia’s
Google, which also runs the Yango Deli grocery service
Russia-Ukraine war: live news
Shanti Das
Sat 5 Mar 2022 15.02 EST
five
GA Yango Deli driver on an electric moped delivers to homes in London. The service is expanding
across the city. Photograph: John Sibley/Reuters
```

## Slide 13

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Data-harvesting code in mobile apps sends user
data to “Russia’s Google”
Data from apps on Apple- and Google-powered mobile devices is sent to Russian servers.
User profiles
AppMetrica: Your app’s
CRM
Build complete audience knowledge with
segmentation based on profile data or dive into
individual users with profile cards.
Today
° © Launch app
= Q Start onboarding
O  Gotocatalog
©) hes
9° @ 0
O  Viewitem
© Addto cart
13
```

## Slide 14

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Article
Russia's war hits Yandex, the ‘Google of Russia’
Sources say the company is seeking a media exit as top exec hit with sanctions over
propaganda charge
TSAKO sh+ Natasha Lomas, Ingrid Lunden 12:20 PM PDT + March 16, 2022
```

## Slide 15

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
= a INSIDER —_—___ ister: Het, mmo
| Premium | HOME > TECH
'| bought a plane ticket and left 12 hours later’: Engineers at Yandex,
Russia's Google rival, are fleeing abroad and leaving spouses and
salaries behind
Rosie Bradbury Apr 12,2022, 3:35 AM PDT Q f [<4] ad
```

## Slide 16

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
REUTERS® World Business v Markets V Sustainability Legal v Breakingviews Technology Investigations More v fo MyViwy Q
Yandex CEO resigns after being targeted
by EU sanctions
Reuters
June 3, 2022 7:35 AM PDT : Updated a year ago Q Aa < |
bas Ne
The logo of Russian internet group Yandex is pictured at the company's headquarter in Moscow, Russia October 4, 2018. REUTERS/Shamil
Zhumatov
June 3 (Reuters) - Russian internet giant Yandex (YNDX.O) said on Friday that Arkady Volozh had stepped
down as CEO and left the board of directors after the European Union included him on its latest list of
sanctions against Russian entities and individuals.
```

## Slide 17

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Yandex's sale of media assets to VK inc
yandex.ru homepage
=
ludes
Login
AM PDT + August 23, 2022
/ 12:05
ptari
Natasha Lomas @ri
Soa
Crunch+
Tect
ups
r=)
Star
2
Security
Al
Crypto
Apps
Events
More
```

## Slide 18

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
REUTERS . World y Businessv Marketsv Sustainability~ Legal Breakingviews Technologyv Investigations More v fo My View v (Oy
Deals
Yandex parent to review ownership of
Russian tech giant, seek divestment
By Alexander Marrow, Darya Korsunskaya and Polina Devitt
November 25, 2022 7:31 AM PST : Updated 8 months ago q | | Aa | < |
```

## Slide 19

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i} REUTERS
a
World vy Businessv Markets Sustainabilityv Legalvy Morev Tl
Europe 30 YEARS 9 4)
Putin, Kudrin touch on future of
Yandex in late-nig ht meeting -sources = NEWS’~ UKRAINEWAR- BUSINESS’ OPINION ARTSANDLIFE PODCASTS
. Moscow Times
INDEPENDENT NEWS FROM RUSSIA
Reuters
Aa
November 25, 2022 4:19 AM PST : Updated 8 months ago W <
Kremlin Ally Kudrin Confirms
“| Move to Tech Giant Yandex
Dec. 5, 2022 f ] © © © iF)
11/2] The logo of Russia
October 4, 2018. REUT!
```

## Slide 20

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Pressonawessre Dy Psp inf =|
ABOUTME CONTACTS NOTACV PROJECTS
YANDEX SERVICES SOURCE
CODE LEAK
SHORT OVERVIEW OF BREACH CONTENTS
Just a few hours ago | found mention on Twitter that proprietary source code of Russian giant
Yandex been leaked on online community called BreachForums. In this post I'll share results of
my friend digging into said archives.
Important details about torrent:
¢ Itjust content of repository without anything else.
All files are dated back to 24 February 2022.
¢ It does not contain git history, mostly just code
¢ No pre-built binaries for most of software with only few exceptions
¢ There are no pre-trained ML models with some exceptions
```

## Slide 21

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
<4 ¢ Support The Moscow 1
The .2, Moscow Times iol
30 YEARS i INDEPENDENT NEWS FROM RUSSIA
= NEWS’ UKRAINEWAR- BUSINESS OPINION ARTSANDLIFE PODCASTS NEWSLETTERS ARCHIVE
Russian Billionaires Line Up to Buy sosreea> stn
Yandex — Reports 1 ama
Russia Says Ukrainian Drone:
Moscow, Crimea
May 4, 2023 600000 2 NO PASSAGE
Russia Blocks Cargo Ship Ov
Traces’
3 POLITICAL PRISONER
Navalny Ally Jailed 9 Years fc
Is
| :
H . : 4 = MoRE MANPOWER
Y Russia Raises Upper-Age Lir
; Y ’ Reservists
MONEY DRAIN
```

## Slide 22

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
World Business Markets v Sustainability Legal’ Breakingviews Technology Investigations More v fo MyViwy Q
Technology
Russia's Yandex fined for refusing to
share user information with security
services
Reuters a a ee
(a | [aa] (<)
June 18, 2023 3:20 PM PDT - Updated a month ago
```

## Slide 23

# Roadmap

●Background on Yandex Leak ●Dive into code: ○What data Yandex is collecting ○What Yandex is doing with that data ○Who Yandex is sharing that data with ●Conclusions and wrap up ●Q&A

23

## Slide 24

## Yandex Codebase

24

## Slide 25

#### Codebase

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Codebase
cS
S
;
-
:
maps_2.tar.bz2 maps_adv.tar.bz2 —— maps.tar.bz2 market.tar.bz2 metrika.tar.bz2 mobile-
WARNIN...L.tar.bz2
fb
LP
nginx.tar.bz2 noc.tar.bz2 partner.tar.bz2 passport.tar.bz2 pay.tar.bz2 payplatform.tar.b
22
U
Paysys.tar.bz2 portal.tar.bz2 — privacy_office.tar. products.tar.bz2 robot.tar.bz2 rt-
bz2 research.tar.bz2
723)
```

## Slide 26

## Metrika

26

## Slide 27

#### Metrika

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Metrika
a] AppMetrica Solutions Features Verticals Resources
Supercharge app
metrics with data
insights
with a one-stop solution for analytics and marketing
Yandex Metrica
All-Round Web Analytics
Features
Resources
From traffic trends to mouse movements —
get a comprehensive understanding of your
online audience and drive business growth.
Get started
et
Try live demo
Pricing
27
|
```

## Slide 28

#### Example Raw Data Fields that AppMetrica Logs

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Example Raw Data Fields that AppMetrica Logs
lytics > appmetrica-location-log-anonymizer > = convert_log.yql analytics > appmetrica-location-log-anonymizer > = convert_log.yql
insert into *//home/metrika-Logs/anonym-appmet rica-location-log/1d/{table_date}* “IsExtraLocationEvent”,
with truncate “IsRooted* ,
select *KitBuildNumber*,
String: :HexEncode(Digest::Blake2B(*DeviceID°, seed)) as ‘DeviceID*, “KitBuildType’,
String: :HexEncode(Digest::Blake2B(*ADVID*, seed)) as “ADVID*, “KitVersion’,
String: :HexEncode(Digest::Blake2B(*IFA*, seed)) as “IFA, ‘Latitude’,
String: :HexEncode(Digest::Blake2B(*UUID*, seed)) as “UUID*, “LatitudeLBs*,
String: :HexEncode (Digest: :Blake2B(*AndroidID*, seed)) as ‘AndroidID*, “LocationAltitude’,
“APIKey*, “LocationDirection’,
~AppBuildNumber* , *LocationEnabled*,
“AppFramework* , “LocationPrecision’,
“AppID*, “LocationPrecisionLBS*,
“AppPlatform* , “LocationSource*,
“AppVersionName’, “LocationSpeed’,
*Cells_AreConnected*, “LocationTimestamp*,
“Cells_CellsIDs*, 13 ‘LocationTimestampBootOffset*,
05 ‘Cells_CountriesCodes*, 138 ‘Longitude’,
106 “Cells_Lacs*, 139 “LongitudeLBs*,
07 ‘Cells_LastVisibleTimeOffset*, 140 “OSApiLevel*,
*Cells_OperatorsIDs*, 141 “OSVersion’,
*Cells_OperatorsNames*, 142 *OperatingSystem’,
“Cells_PhysicalsCellsIDs*, 143 “OriginalCollectTimestamp*,
*Cells_SignalsStrengths*, 144 *OriginalLocationTimestamp*,
*Cells_Types*, 145 *ReceiveTimestamp*,
“ChargeType*, 146 *RequestID*,
*ClientIP*, 147 *SendTimestamp* ,
*“ClientIPHash*, 148 *Wifi_AreConnected*,
“CollectTimestamp*, 149 ‘Wifi_LastVisibleTimeOffset*,
“CollectTimestampBootOffset*, 150 ‘Wifi_Macs*,
8 *CollectionMode’, 151 ‘Wifi_SignalsStrengths*,
119 “DeviceType*, 152 ‘Wifi_Ssids*,
12 ‘EventID*, 153 »_logfeller_index_bucket*,
21 “IncrementalID*, 154 »_logfeller_timestamp*,
~IsExtraLocationEvent*, 155 rest*,
“IsRooted*, 156 *_stbx’,
124 *KitBuildNumber” , 1 *iso_eventtime’,
125 *KitBuildType*, 158 ‘source_uri® ,
2¢€ “KitVersion*, 159 *subkey*,
in11 2 -
28
```

## Slide 29

#### Anonymized identifiers

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Anonymized identifiers
Q1
select
String: :HexEncode(Digest::Blake2B(*DeviceID’, seed)) as “DeviceID’,
String: :HexEncode(Digest::Blake2B(*ADVID*, seed)) as “ADVID*,
String: :HexEncode(Digest::Blake2B(*IFA*, seed)) as “IFA‘,
String: :HexEncode(Digest::Blake2B(*UUID*, seed)) as “UUID*,
String: :HexEncode(Digest: :Blake2B(*AndroidID*, seed)) as ‘AndroidID*,
29
```

## Slide 30

#### Location Fields

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Location Fields
126
127
128
129
130
Bs
132
133
134
35
136
137
138
139
140
141
142
143
144
“KitVersion ,
‘Latitude’,
‘LatitudeLBS*,
*LocationAltitude’,
‘LocationDirection ,
“LocationEnabled*,
‘LocationPrecision,
“LocationPrecisionLBS’,
‘LocationSource’,
‘LocationSpeed’,
“LocationTimestamp’,
‘LocationTimestampBootOffset’,
‘Longitude’,
“LongitudeLBs’,
“OSApiLevel’,
“OSVersion’,
‘OperatingSystem ,
“OriginalCollectTimestamp ,
‘OriginallocationTimestamn«
30
```

## Slide 31

#### Wifi Fields Collected By AppMetrica

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wifi Fields Collected By AppMetrica
147
148
149
150
151
152
LoS
*SendTimestamp ,
“Wifi_AreConnected’,
‘Wifi_LastVisibleTimeOffset>
‘Wifi Macs’,
‘Wifi_SignalsStrengths ,
“Wifi_Ssids’,
‘loafeller index bucket’,
31
```

## Slide 32

#### Those fields in Crypta

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Those fields in Crypta
graph > fuzzy > lib > yql > = export_ssid_devid_day_table.yq]
26
27
28
29
30
31
32
33
34
35
36
$list_metrika_log = (
)5
select coalesce(DeviceID, "") as DeviceID,
coalesce(OriginalDevicelD, "") as OriginalDeviceID,
SMakeStringList(Witi_Macs) aS Wifi Macs,
$MakeStringList(Wifi_Ssids) as Wifi_Ssids,
$MakeIntList(Wifi_SignalsStrengths) as Wifi_SignalsStrengths,
$MakeIntList(Wifi_AreConnected) as Wifi_AreConnected
from ‘{source_mmetric_table}*
where DeviceID is not null
32
```

## Slide 33

#### Dev Id and SSID Associated with Yandex UID

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dev Id and SSID Associated with Yandex UID
graph > fuzzy > lib > yql >
6)
7
8
,
10
fa
12
13
14
1D
1A
$mobile_all_table = (
export_ssid_yuids.yql
select distinct mmetric_devid, ssid
from concat({sources})
};
$mmetric_to_devid = (
select mmetric_devid,
coalesce(cast(
devid,
yuid as uint64), @) as yuid
from ‘{source_nolimit_table}*
i;
33
```

## Slide 34

Click Event Data Being Matched to Existing Users

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Click Event Data Being Matched to Existing Users
core > programs > clicklogd-mobile > src > C event_indexed_pool.h > ¢g TEventIndexedPool > © Getindex<TMatchCriteria>()
58 private:
59 template <class TMatchCriteria>
60 TIndex<TMatchCriteria>& GetIndex() {
61 if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TAndroidId>) {
cy return AndroidId_;
63 1} else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TAndroidIdMd5>) {
64 return AndroidIdMd5_;
65 1} else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TAndroidIdSha1>) {
66 return AndroidIdSha1_;
67 } else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TDeviceIdHash>) {
68 return DeviceIdHash ;
69 else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TFingerprint>) {
i) return Fingerprin
else if constexpr (std
return GoogleAid_;
} else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TGoogleAidMd5>) {
return GoogleAidMd5_;
75 } else if constexpr (std
return GoogleAidSha1_;|
HW else if constexpr (std:
return Ifa_;
} else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TIfaMd5>) {
return IfaMd5_;
'S_same_v<IMatchcriteria, NMatchCriteria::TGoogleAid>) {
Bones
is_same_v<TMatchCriteria, NMatchCriteria: :TGoogleAidShal>) fi
s_same_v<TMatchCriteria, NMatchCriteria::TIfa>) {
81 } else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TIfaShal>) {
82 return IfaShal_;
83 } else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TWindowsAid>) {
84 return WindowsAid_}
85 } else if constexpr (std::is_same_v<TMatchCriteria, NMatchCriteria::TWindowsAidMd5>) {
86 return WindowsAidMd5,
87 } else if constexpr (std s_same_v<TMatchCriteria, NMatchCriteria::TWindowsAidShal>) {
88 return WindowsAidSha1.
89 } else if constexpr (std _same_v<TMatchCriteria, NMatchCriteria::TYmTrackingId>) {
90 return YmTrackingId_;
91 Ly
34
```

## Slide 35

#### Socio-Demographic Attributes for DevID being Updated

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Socio-Demographic Attributes for DevID being Updated
core > programs > socdem-updaterd-mobile > src > G UserldAndinfoParser.cpp > ...
L
45 {"0_17", AgeIntervalsCrypta: :LessThan18},
6 {"18_24", AgeIntervalsCrypta: :Between18and24},
{"25_34", AgeIntervalsCrypta: : Between25and34},
{"35_44", AgeIntervalsCrypta: :Between35and44},
{"45_54", AgeIntervalsCrypta: :Between45and54},
{"55_99", AgeIntervalsCrypta: :MoreThan55}
ts
r:setValue(value, exact_socdem_node, key, json_keys_to_ages_intervals) ;
55 void UserIdAndInfoParser: :setValue(
56 SexTypesCrypta & value,
const NYT::TNode & exact_socdem_node,
const TString key)
9 ¢{
60 static const std::map<TString, SexTypesCrypta> json_keys_to_sex_types =
6 {
62 {"f", SexTypesCrypta::Female},
63 {"m", SexTypesCrypta: :Male}
+
65 risetValue(value, exact_socdem_node, key, json_keys_to_sex_types) ;
66}
68 std::string UserIdAndInfoParser::parse(const NYT::TNode & user_record)
69 =f
1) const TString &{device_id = user_record["appmetrica_devid"] .AsString(); |
] UserInfo user_in?o;
const auto & exact_socdem = user_record["exact_socdem"] ;
setValue(user_info.age, exact_socdem, “age_segment");
setValue(user_info.sex, exact_socdem, "gender");
7 static const auto tail = getConstTail();
std::ostringstream buffer;
buffer <<
81 sipHash64(device_id.data(), device_id.size()) << ‘\t' <
LORE AG | 2 1s
35
```

## Slide 36

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Supexc Ayautopun
Create segments based on
offline and online data
Create Segment
Slumexc Ayautonuu
JloanbHble KNNeHTbI
CermenTet
| 582685 =) Te 73% 27%
To come in
36
```

## Slide 37

## Crypta

37

## Slide 38

#### Crypta

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Crypta
Yandex COMPANY JOBS FORDEVELOPERS FORADVERTISERS FOR INVESTORS
About History Privacy PressReleases Blog Contact Qo
Technologies /
Crypta
Every day, millions of web users are exposed to banner ads on the pages of Yandex's sites. Advertisers on
Yandex can opt to show their ads only to that part of the viewer audience that is potentially interested in
seeing them, such as people of a certain age or gender. To enable advertisers to target their ads to a specific
audience, Yandex uses its own proprietary behavior analytics technology called Crypta. This technology allows
classification of web users based on their online behavior. Their behaviour just has to differ somehow.
38
```

## Slide 39

#### Example Segments

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Example Segments
v CRYPTA
e*ee@e@v
eee
ete
eee eee
e*e?ee@¢
*
eee @
test
age_segment_18_20.py
alice_users.py
apartment_room_number.py
apps_users.py
artists.py
auto_interactions.py
avia_travellers.py
bank_cards.py
bought_two_tickets.py
business_travellers.py
children_age_segment_clarification.py
compulsory_auto_insurance.py
connection_type.py
console_gamers.py
contest.py
devices_without_google_services.py
digital_viewers.py
direct_clients_by_industry.py
direct_product_users.py
disk_users.py
ecommerce_owners.py
edadeal_offline_purchases_lal.py
expensive_car_customers.py
film_lovers_by_genres.py
gas_stations.py
industry_representatives.py
kbt_customers.py
kfc_visitors.py
kinopoisk_logins.py
kinopoisk_movie_watchers.py
Reo ea
~ CRYPTA
ee??? @@@2022000080
e??e? @@2200704
?\2 @
eee 02208
kinopoisk_movie_watchers.py
kz_users.py
laptop_users.py
logged_in_for_plus.py
longterm_interest_mobile_gamers.py
loyal_to_launcher_install.py
macos_users.py
mail_data.py
manufacturer_phone_owners.py
marketplaces_Itv_users.py
mobile_gamers.py
mobile_operators_users_by_prefix.py
mobile_operators_users.py
multidevice_puid.py
multidevice.py
music_genres_listeners.py
nestle_regions.py
phone_buyers.py
phone_owners.py
phone_with_esim_owners.py
potential_aon_android_users.py
potential_aon_ios_users.py
preinstalled_apps.py
prism.py
proleads.py
realty_interactions.py
recent_passport_accounts.py
score_users_for_telephony.py
searched_for_phone_numbers.py
searched_radisson_on_maps.py
\ CRYPTA
STS AHCESC ESE te ee ee ee eee
e+? 2008
OT PONTE STC TOT
mobile_operators_users_by_prefix.py
mobile_operators_users.py
multidevice_puid.py
multidevice.py
music_genres_listeners.py
nestle_regions.py
phone_buyers.py
phone_owners.py
phone_with_esim_owners.py
potential_aon_android_users.py
potential_aon_ios_users.py
preinstalled_apps.py
prism.py
proleads.py
realty_interactions.py
recent_passport_accounts.py
score_users_for_telephony.py
searched_for_phone_numbers.py
searched_radisson_on_maps.py
seo_specialists.py
seo_users.py
smart_gadgets_customers.py
smokers.py
summer_residents.py
travellers.py
video_bloggers.py
want_to_change_the_provider.py
webmaster.py
widgets.py
with_children_by_ages.py
a make
TOTSE
GReOe
TOUTSTTTTET
39
```

## Slide 40

#### Example Segments

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Example Segments
??@??2?20020 @
v
smart_gadgets_customers.py
smokers.py
summer_residents.py
travellers.py
video_bloggers.py
want_to_change_the_provider.py
webmaster.py
widgets.py
with_children_by_ages.py
va make
40
```

## Slide 41

#### Travellers

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Travellers
profile > runners > segments > lib > coded_segments > ® travellers.py > ...
82
83 INSERT INTO ‘{output_table}* WITH TRUNCATE
84 SELECT
85 id,
86 id_type,
87 segment_name
88 FROM(
89 SELECT
90 crypta_id AS id,
91 ‘crypta_id' AS id type,
92 CASE
93 WHEN Geo: :RoundRegionById(region, “country").id != Geo::RoundRegionById(CAST(main_region AS Int32), “country").id THEN ‘internati
94 ELSE ‘domestic’
95 ~END-ASsegment_name,
96 MAX(*date*>) AS last_seen,
97 MIN(*date*) AS first_seen,
98 region,
99 week_end_date,
100 FROM $travell_visits
101 GROUP BY region, main_region, crypta_id, week_end_date
102.—)
103 WHERE
104 last_seen <= week_end_date AND
105 DateTime: : ToDays (DateTime: :MakeTimestamp($parse(last_seen)) —- DateTime: :MakeTimestamp($parse(first_seen))) > @ AND
106 DateTime: : ToDays (DateTime: :MakeTimestamp($parse(week_end_date)) - DateTime: :MakeTimestamp($parse(first_seen))) <= 7
107. GROUP BY id, id_type, segment_name
108 ue
109
118
41
```

## Slide 42

#### Mail Data

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Mail Data
profile > runners > segments > lib > coded_segments > @ mail_data.py > ...
12
13
14 segment_query = """
15 INSERT INTO ‘{output_table}* WITH TRUNCATE
16 SELECT id, id_type, segment_name
17 FROM *{mail_data_table}*;
18
19 INSERT INTO ‘{sample_table}* WITH TRUNCATE
20 SELECT,
21 yandexuid,
22 segment_name
23 FROM (
24 SELECT matching. yandexuid AS yandexuid, mail_data.segment_name AS segment_name
25 FROM ‘{mail_data_table}* AS mail_data
26 INNER JOIN ‘{indevice_yandexuid_matching}* AS matching
27 USING (id, id_type)
28 )
29 GROUP BY yandexuid, segment_name
30 uae
spl
32
BS class PrepareMailSampleForLalSegments(RegularSegmentBuilder) :
34 keyword = 549
65 name_segment_dict = {
36 ‘aviaticket': 1404,
y/ "boardingpass': 1405,
38 "hotel': 1406,
39 }
42
```

## Slide 43

#### Gas Stations

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Gas Stations
profile > runners > segments > lib > coded_segments > @ gas_stations.py > ...
92
2}
94
95
96
o7
98
O95
100
101
102
103
104
105
106
107
108
109
110
111
a2
class ProcessedDeepVisitLogForGasStations(DayProcessor):
def requires(self):
return deep_visits.org_visits_deep_external_input(self.date)
def process_day(self, inputs, output_path):
self.yql. query (
gas_stations_query_temp late. format (
organization_categories=config.ORGANIZATION_CATEGORIES,
deep_visits=inputs.table,
matching_idfa=get_matching_table('idfa', ‘crypta_id'),
matching_gaid=get_matching_table('gaid', ‘crypta_id'),
name_to_variable=',\n'.join(
[u'("{}", "{}")'.format(key, value)
for key, value in name_to_variable.iteritems()]
,
output_table=output_path,
),
transaction=self.transaction,
43
```

## Slide 44

#### Example ML Model Types

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Example ML Model Types
~ CRYPTA
*@
eee
eee
eee
tee ee tees eevee
*
RROse
legal_entities_model_application.py
legal_entities_model_training.py
its_model_application.py
legal_office_)
legal_office_visits_model_training.py
market_model_application.py
market_model_training.py
market_rfm_model_application.py
market_rfm_model_training.py
marriage_model_application.py
marriage_model_training.py
medical_clinic_model_application.py
medical_clinic_model_training.py
mortgage_approval_model_application.py
mortgage_approval_model_training.py
online_cinema_model_application.py
online_cinema_model_training.py
online_payment_model_application.py
online_payment_model_training.py
online_sales_register_model_application.py
online_sales_register_model_training.py
online_shopping_model_application.py
online_shopping_model_training.py
pharmacy_model_application.py
pharmacy_model_training.py
realty_visit_model_application.py
realty_visit_model_training.py
tv_viewers_model_application.py
tv_viewers_model_training.py
windows_installation_model_application.py
windows_installation_model_training.py
va make.
44
```

## Slide 45

#### Basic example of household details

45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Basic example of household details
78
79
graph > metrics > household > & query.sq!
44
45
46
FROM $composition
GROUP BY $size_to_range(size) AS key;
END DEFINE;
DEFINE SUBQUERY $hh size by crypta id($title, $predicat) AS
SELECT
($title || key) AS key,
COUNT(1) AS hh_size_by_crypta_id
FROM $composition
WHERE $predicat(size, socdems)
GROUP BY CAST(Yson::GetLength(Yson::Lookup(data, ‘crypta_ids')) AS String) AS key;
END DEFINE;
DEFINE SUBQUERY $hh_by_socdems($title, $predicat) AS
$hh_socdem = (
SELECT
hhid,
size,
IF((Yson::LookupInt64(info, 'female') @), ‘female’, Null) AS has_female,
IF((Yson::LookupInt64(info, ‘male') != @), ‘male’, Null) AS has_male,
IF((Yson::LookupInt64(info, ‘grand') != @), ‘grand', Null) AS has_old,
IF((Yson::LookupInt64(info, ‘child') != @), ‘child', Null) AS has_child
FROM $composition
WHERE $predicat(size, socdems)
;
SELECT ($title || groups) AS key, hh_c AS hh_socdem_count
FROM (
SELECT groups, SUM(size) AS hh_c
FROM $hh_socdem
GROUP BY String::JoinFromList(
Listsort(AsList(has female, has mate, has old, has child).
*_') AS groups
) WHERE groups != "";
END DEFINE;
45
```

## Slide 46

AppMetrica being used to pull wifi connection types:

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AppMetrica being used to pull wifi
connection types:
profile > runners > segments > lib > coded_segments > ® connection_type.py
9 connection_type_query = """
@ INSERT INTO ‘{output_table}” WITH TRUNCATE
SELECT
AS id_type,
5 WHEN types
6€ WHEN types
ELSE '3g_4g'
f END AS segment_name
9 FROM (
® SELECT
id,
ToSet (AGGREGATE_LIST_DISTINCT(segment_name)) AS types
FROM *{input_table}
GROUP BY id
AsSet('3g') THEN ‘3g'
AsSet('4g') THEN ‘4g'
¢ class ConnectionType(RegularSegmentBuilder):
80 name_segment_dict = {
'3g': (557, 17823841),
‘4g': (557, 17823853),
"3g_4g': (557, 17823847),
BE number_of_days = 35
BE def requires(self):
9 return {
3¢ “AppMet ri : LogProcessor(
ProcessAppMet ricaForConnectionType,
self.date,
self.number_of_days,
46
```

## Slide 47

##### AppMetrica data being used to separate users with common SSIDs (wifi networks)

47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AppMetrica data being used to separate users with common
SSIDs (wifi networks)
class ImportSsidMobileMetrikalask(BaseTask):
date = DateParameter()
SSID_THRESHOLD = 20
YUID_THRESHOLD = 20
DAYS_IN_MONTH = 7
def requires(self):
asks must be done to complete this task
task_list = [
ImportSsidMobileMetrikaDayTask(date=self.date, target_date=target_date, ssid_threshold=self.SSID_THRESHOLD)
for target_date in days_range_back(self.date, self.DAYS_IN_ MONTH)
]
return task_list
47
```

## Slide 48

AppMetrica data being used to separate users with common SSIDs (wifi networks)

48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AppMetrica data being used to separate users with common
SSIDs (wifi networks)
def _run(self):
self.yt.create_table_with_schema(
self.destination, self.destination_schema, strict=True, recreate_if_exists=True
)
with self.yt.TempTable() as unexploded, self.yt.TempTable() as not_unique:
self.yql.execute(self.query(unexploded), syntax_version=1)
run_native_reduce(
reducer_name="NCommonWif iAP: :TExploder",
source=unexploded,
destination=not_unique,
proxy=self.yt.proxy,
transaction=self.yt.transaction_id,
pool=conf.Yt.POOL,
title="Explode yandexuids with common wifi access point",
reduce_by=["ssid"],
)
yuid_pair = [conf.Constants.YUID_LEFT, conf.Constants.YUID_RIGHT]
self.yt.run_sort(not_unique, not_unique, sort_by=yuid_pair)
run_native_reduce(
reducer_name="NCommonWif iAP: : TUnique",
source=not_unique,
destination=self.destination,
proxy=self.yt.proxy,
transaction=self.yt.transaction_id,
pool=conf.Yt.POOL,
title="Make yandexuids with common wifi access point unique",
reduce_by=yuid_pair,
)
self.yt.run_sort(self.destination, sort_by=yuid_pair)
self.yt.set(self.destination + "/@generate_date", self.date. isoformat())
48
```

## Slide 49

#### Sources

Search Data Wifi

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Sources
graph > fuzzy > lib > ®@ config.py > ¢ GeoPaths
class SourceTypes(object):
EMAIL_LOGIN = "EMAIL LOGINS"
EMAIL_SIMILAR = “EMAIL SIMILAR"
GEO_HOMEWORK = "GEO HOMEWORK"
HOUSEHOLD = "HOUSEHOLD"
REQANS_LOG = “REQANS LOG" ——= Search Data
SSID = "SSID" ——\Vifj
49
```

## Slide 50

#### Yandex IDs Associated with Email

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Yandex IDs Associated with Email
class EmailPaths(object):
ROOT = ROOT
# Emails
BASE = "{root}/email". format(root=RO0T)
ALL_EMAILS_TABLE = "{base}/all_emails". format (base=BASE)
ALL_EMAIL_LOGINS_TABLE = "{base}/all_email_logins". format (base=BASE)
ALL_EMAILS_SORTED_BY_LOGIN = "{base}/all_email_logins.sorted_by_login". format (base=BASE)
ALL_EMAIL_LOGINS_PAIRS_TABLE = "{base}/all_email_logins.pairs". format (base=BASE)
ALL_EMAILS GROUPED_BY_LOGIN = "{base}/all_email_logins.groups". format (base=BASE)
ALL_YUID_PAIRS_FROM_EMAIL_LOGIN = "{base}/all_yuid_pairs_from_email_logins_matching". format (base=BASE)
ALL_YUID_PAIRS_FROM_SIMILAR_EMAILS = "{base}/all_yuid_pairs_from_similar_emails". format (base=BASE)
ALL_EMAILS_TABLE_SCHEMA = {"emai "string", "yuids": “any"}
ALL_EMAIL_LOGINS_TABLE_SCHEMA = {"login": "string", "email": "string", “yuids": "“any"}
ALL_EMAILS SORTED_BY_LOGIN_SCHEMA ="{"login’: string’, "emarl’: "string’, "yulds’: "any" }
ALL_EMAILS_GROUPED_BY_LOGIN_SCHEMA = {"login": "string", "all_emails": "any", “howmany": "uint64"}
ALL_EMAIL_LOGINS_PAIRS_TABLE_SCHEMA = {
“email_1": "string",
“email_2": "string",
“Login”: "string",
“yuids_1": “any",
“yuids_2": "any",
}
ALL_YUID_PAIRS_FROM_EMAIL_LOGIN_SCHEMA = {
Constants. YUID_LEFT: (“uint64", True),
Constants. YUID_RIGHT: ("uint64", True),
"match": "any",
}
ALL_YUID_PAIRS_FROM_SIMILAR_EMAILS SCHEMA = {
Constants. YUID_LEFT: “uint64",
Constants. YUID_RIGHT: “uint64",
"“email_left": “string”,
“email_right": "string",
“fragment": “string”,
```

## Slide 51

#### Login Data

Extracting multiple types of identifiers

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Login Data
graph > fuzzy > lib > tasks > sources > visitlog_logins > ® extract.py > ...
aeT Tllter_rare_logins_optlons(setT):
return TFilterRareLoginsOptions(Threshold=self.threshold).SerializeToString()
@property
def filter_keys_options(self):
return TFilterKeysOptions(
Keywords=[
"Login",
“user”,
“userid”,
“clientid",
"uid",
“email”,
“emailhash",
"\u043b\u043e\u0433\Uu0438\u043d",
“computerid",
"cid",
“suserid",
]
).SerializeToString()
Extracting
multiple types
of identifiers
51
```

## Slide 52

#### Passport

52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Passport
= c
@ cyberChet
@ passport.yandex.com,
©) confiant-inc/priva... [3 Tracker DBs
punt, y
2t dire
tions and u
[i Reading [%j Useful snippets
Yandex
@ hittps://emplist.co...
@ https:j/vendor-list..
1% Consent String De...
Registration
Technique protect...
52
```

## Slide 53

#### Passport User ID Associated with Phone

53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Passport User ID Associated with Phone
graph > data_import > passport > lib > query > = passport.sql
33
34 $out_login_tbl = $soup_output_dir || $edge(IdType::PUID(), IdType::PHONE(), SourceType::PASSPORT_PROFILE(), LogSource: : PASSPORT_PHONE_DUMP( ) ) ;
3 INSERT INTO $out_login_tbl WITH TRUNCATE
SELECT
37 id1,
38 IdType::PUID() AS id1Type,
39 id2,
IdType::PHONE() AS id2Type,
SourceType: : PASSPORT_PROFILE() AS sourceType,
LogSource: : PASSPORT_PHONE_DUMP() AS logSource,
é ListCreate(String) AS dates
44 FROM (
45 SELECT DISTINCT puid, phone
4 FROM $log FLATTEN LIST BY phones AS phone
) WHERE Identifiers: : IsSignificantPhone(phone)
GROUP BY
puid AS id1,
50 phone AS id2
53
```

## Slide 54

54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
graph > data_import > passport > tests > fixtures > {} passport.json > ...
al
O©MNMRURWHN
10
11
12
13
14
15
16
17
18
19
20
pak
22
23
24
PAs)
26
ZT,
28
29
30
31
32
{"uid":
{"uid"
{"uid"
{"ui
{"uid"
{"uid"
{ui
{"uil
{"ui
{"uid
{"uid"
{"uid"
{"uid":
{"uid"
{"uid"
{"uid"
{"uid"
{"uid"
{"uid"
{"uid"
{"uid"
{"uid"
{"uid"
Obie hg
{"uid":
{"uid":
{"uid":
{"uid"
{"uid"
{"uid"
"11111", "login":
#11112", “login
"11113", "login
"11114", “login
"11115", "login"
"11116", "login"
"11117", "login"
11118"; “login™
"11119", "login
"11120", "login
"11121", "login
#11122", “login
"11123", "login
"11124", “login
"11125", "login"
"11126", "login"
"11127", "login"
11128", “Login™
"11129",
"123456",
"123457",
“aashinova"}
“andrei-ponomareff-1997"}
“anoshko-av"}
“bars12@161. ru"}
“evOngertlt"}
“evarcher"}
"Lagutin2008"}
“login-for-avito"}
“modsever"}
“mouradian"}
“perschina-olga2013"}
“r.amiras lanov@dveri. ru"}
“saprovec2015"}
“stoltat"}
"“sveta—aleshina2015"}
“watchradius"}
“watchradius"}
"sveta-aleshina2015"}
“watchradiusmob"}
“abc127", "phone_numbers'
“abc123", "phone_numbers"
{1}
["+1234567890", "+71111234567"]}
"123458", "login": "", "phone_numbers": ["+9393939393", "+71202020201"]}
"134614616", "login": “roscosh8"}
"134648582", “login": “e222mn"}
"15033290", "login": "mouradian"}
"194502233", "login": "ingvr80"}
"2687", “login": “govshit"}
"2687", "login": "GOVSHIT"}
"76667777", “login": "g8jkqqaaaaaaaaah"}
"766679666", "login": “d6fqqaaaaaaaaah"}
: "766679777", "login": "mdmozn45"}
54
```

## Slide 55

#### Crypta - Geo graphs

Using lat/long data associated with “predicted home”, linked to Yandex UID

55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Crypta - Geo grap
Using lat/long
data associated
with “predicted
home’, linked to
Yandex UID
as
graph > fuzzy
lib > tasks > sources > geo > C geo_operations.h
void Do(TTableReader<TNode>* input, TTableWriter<TGeoSquare>* output)
override {
for
input->IsValid( input->Next()) {
t auto& row = input->GetRow();
if (not IsRowValid(row)) {
continue;
t ui64 yandexuid = FromString<ui64>(row|"yandexuid"] .AsString());
auto& homeCoordinates = row|"predicted_home"'];
latitude = homeCoordinates |" latitude"] .AsDouble();
to longitude = homeCoordinates |" longitude") .AsDouble( ) ;
onst
onst auto& square = computeSquare({.Lat = latitude, .Lon = longitude}, State->radius());
for (int beltOffset : {-1, @, 1}
for (int sqoffset : {-1, 0}
if (beltoffset
continue;
-1 & sq0ffset == 0) {
+
ynst ui64 square_idx = ConvertSquareToIdx({.Belt =
TGeoSquare out;
out. set_yandexuid(yandexuid) ;
out.set_lat( latitude) ;
out.set_lon( Longitude) ;
out. set_squareidx(square_idx) ;
output->AddRow( out);
square.Belt + belt0ffset, .Sq =
square.Sq + sq0ffset
54
```

## Slide 56

#### Crypta - Geo graphs

Then using that data to find literal neighbors within a certain radius of that home

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Crypta - Geo graphs
Then using that
data to find
literal neighbors
within a certain
radius of that
home
public:
lib > tasks > sources > geo > C geo_operations.h
TEindNeighbors: public IReducer<TTableReader<TGeoSquare>, TTableWriter<TNeighborsDistance>> {
TFindNeighbors (
: State(
TFindNeighbors(const TBuffer& buffer
: State(buffer
d Do(TTableReader<TGeoSquare>* input, TTableWriter<TNeighborsDistance>* output) override
‘onst double radius = State->radius();
TVector<TGeoSquare> candidates;
for (; input->IsValid(); input->Next()) {
const auto& row = input->GetRow();
candidates. push_back( row) ;
xrange(candidates.size())) {
for (auto j : xrange(i + 1, candidates.size()
suto& left = candidates.at(i);
const auto& right = candidates.at(j);
if (left.yandexuid() == right. yandexuid()
continue;
distance = computeDistance({.Lat = left.lat(), .Lon = left.lon()}, {.Lat =
distance > radius
inu
‘TNeighborsDistance out;
out. set_distance(distance) ;
out. set_yandexuidleft (Min( left. yandexuid(), right.yandexuid()));
out. set_yandexuidright (Max(left.yandexuid(), right. yandexuid()));
output->AddRow(out) ;
```

## Slide 57

#### AppMetrica and Taxi data being used generate segments about households with children:

57

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AppMetrica and Taxi data being used generate segments
about households with children:
self.yql.query(
2pp_metrica query. format (
devid_by_app_table=self.input() ['DevidByApp'].table,
Output_table=with children by app table
app_to_segment_name='\n'.join(app_segment_name_tuples),
yy
transaction=self.transaction,
build_segment(self, inputs, output_path):
with self.yt.TempTable() as taxi_puid_table, \
self.yt.TempTable() as app_metri table:
self.yt. run_map(
extract children from taxi
inputs ['TaxiData'].table,
taxi_puid_table,
self.prepare_with_children_by_app(app_metrica_table)
self.yql.query(
with_children_query_template. format (
metrics_table=inputs['ProcessedMetrics'].table,
reqans_table=inputs|['ProcessedReqans'].table,
app_metrica_table=app_metrica_table,
taxi_data_table=taxi_puid_table,
id_to_crypta_id_table=config.VERTICES_NO_MULTI_PROFILE,
crypta_id_to_hhid_table=config.HOUSEHOLD_CRYPTA_ID_TO_HHID,
yandexuid_to_hhid_table=config.HOUSEHOLD_REVERSED_TABLE,
hhid_to_yandexuid_table=config.HOUSEHOLD_ENRICH_TABLE,
output_table=output_path,
57
```

## Slide 58

#### ID mapping associations:

58

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ID mapping associations:
taxi_data_table=taxi_puid_table,
id_to_crypta_id_table=config. VERTICES NO_MULTI_PROFILE,
crypta_id_to_hhid_table=config.HOUSEHOLD_CRYPTA_ID_TO_HHID,
yandexuid_to_hhid_table=config.HOUSEHOLD_REVERSED_TABLE,
hhid_to_yandexuid_table=config.HOUSEHOLD ENRICH TABLE,
output_table=output_path,
58
```

## Slide 59

Profiles integrate biometric data, most likely from smart speakers that use Yandex’s Alice smart assistant

59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Profiles integrate biometric data, most likely from smart
speakers that use Yandex’s Alice smart assistant
Yandex COMPANY JOBS FOR DEVELOPERS FOR ADVERTISERS FQ
About History Privacy Press Releases Blog Contact
Press Releases / 2022 /
Yandex Launches Smart Devices With Alice in
Uzbekistan
Internet, November 22, 2022. Uzbekistan’s local
Stations with Alice. Upon purchasing a smart s|
pene e P Stations are smart speakers with Alice. A single Yandex Plus subscription allows you to play music, podcasts,
or playlists with personal recommendations on Yandex Station. Alice, the voice assistant on board, can
entertain children with an educational game or compose a fairy tale together. She will tell you about the
weather or remind you to buy groceries. Alice loves talking and will hold a conversation with ease: currently, in
Russian only.
59
```

## Slide 60

#### Possible Children by Voice

60

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Possib
e Children by Voice
profile > runners > segments > lib > coded_segments > ® children_age_segment_clarification.py > ..
13 clarify_children_yql_template =
14 $possible_children_by_voice = (
15 SELECT ‘uuid’, TableName() AS ‘date’, '@_12' AS segment_name
16 FROM RANGE(* {biometry folder}*, “{biometry_first_date}’, *{biometry_last_date}’)
17 WHERE bio_child > 0.8
18 3
19
20 Spossible children by voice = (
21 SELECT DISTINCT “uuid’, ‘date’, segment_name
22 FROM $possible_children_by_voice
23);
24
25 $possible children by voice = (
26 SELECT “uuid’, segment_name
27 FROM $possible_children_by_voice
28 GROUP BY ‘uuid*, segment_name
29 HAVING COUNT(*) >= 2
30 3
31
32 $sources_new_age = (
33 SELECT matching.cryptaId AS cryptaId,
34 CASE
35 WHEN socdem storage.birth date > ‘{thirteenth birthday}' THEN '@ 12°
36 WHEN ‘{thirteenth_birthday}' >= socdem_storage.birth_date AND
37 socdem_storage.birth_date > '{eighteenth_birthday}' THEN '13_17'
38 ELSE '18_99°
39 END AS segment_name
40 FROM ‘{socdem_storage_table}* AS socdem_storage
41 INNER JOIN ‘{id_to_crypta_id_table}* AS matching
42 ON socdem_storage.id == matching.id AND socdem_storage.id_type == matching. id_type
43 WHERE socdem_storage.birth_date is not Null
44 UNION ALL
45 SELECT matching.cryptaId AS cryptaId, biometry.segment_name AS segment_name
46 FROM $possible_children_by_voice AS biometry
47 INNER JOIN ‘{id_to_crypta_id_table}’ AS matching
48 ON biometry. *uuid* matching. id
40. WHERE match dat. aoe id
60
```

## Slide 61

UI for Infographics Card

61

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
_UI for Infographics Card
const marriedText = convertMarriedToSingleText(exactDemographics.gender, married);
const incomeText = convertIncomeSegmentToText (exactDemographics. income) ;
const hasChildrenText = convertHasChildrenToText(hasChildren) ;
return (
<div className="BasicInfoGraphics">
<img alt="" className="BasicInfoGraphics—Image" src={images [exactDemographics.gender] }/>
<div “BasicInfoGraphics-Bubble BasicInfoGraphics—Bubble_family">{marriedText}</div>
<div BasicInfoGraphics-Bubble BasicInfoGraphics—Bubble_income">{incomeText}</div>
<div BasicInfoGraphics-Bubble BasicInfoGraphics—Bubble_children">{hasChildrenText}</div>
<div className="BasicInfoGraphics-Interest BasicInfoGraphics-Interest_first">
<div className="BasicInfoGraphics—InterestIcon"
style={{ backgroundImage: ‘url(${interestIcons(6]})> }}/>
</div>
<div className="BasicInfoGraphics-Interest BasicInfoGraphics-Interest_second">
<div className="BasicInfoGraphics-InterestIcon"
style={{ backgroundImage: ‘url(${interestIcons[1]})> }}/>
</div>
<div className="BasicInfoGraphics-Interest BasicInfoGraphics-Interest_third">
<div className="BasicInfoGraphics-InterestIcon"
style={{ backgroundImage: ‘url(${interestIcons[2]})* }}/>
© icons
> apps
~ interests
"@ agro.svg
animals.svg
appliances.svg
beauty.svg
business.svg
clothes.svg
construction.svg
=
=
=
=
=
‘mw education.svg
“a electronics.svg
"m entertainments.svg
“a family.svg
‘a finance.svg
"w food.svg
‘a gifts.svg
Js index.js
job.svg
realty.svg
rest.svg
sport.svg
stationery.svg
telecom.svg
61
ewnrnrnrse
transport.svg
```

## Slide 62

#### Search Profile by ID

62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Search Profile by ID
web > portal > src > graph > search > JS SearchPanel.js > ...
return (
<div key={"inputs—" + suffix} className="input-group">
14 <div style={{display: showIdInput ? "block" : "none"}}>
<ValueInput
key="id_value"
placeholder="[id value]"
value={parameters ["idValue" + suffix]}
onChange={changeParameter("uid" + suffix)}
return (
experiments.status !== 403 && (
<div className="experiments—bar">
<div className="experiments-select-uid-type">
<RadioButton
value={act iveUid}
size="5"
view="default"
className="select-sorting"
onChange={(event) => selectUidType(event.target.value) }
options=((j
{ value: "uid", children: t("by") + " yandexuid" },
{ value: “cryptaId", children: t("by") + " CryptaID" },|
|
iD
62
```

## Slide 63

#### UI - Available App Icons

63

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
UI - Available App Icons
v CRYPTA GBRoae
4S Timedinterests.js
JS utils.js
> pages
\ public-info
> components
v icons
v apps
v comyandex.browser
fa active.svg
fa disabled.svg
com yandex.browser.lite
com yandex.lavka
>
>
> comyandex.mobile.drive
> comyandex.music.auto
>
com yandex.music.xiaomi
com yandex.toloka.androidapp
Y comyandex.zen
"m active.svg
fa disabled.svg
default
ruyandex.androidkeyboard
ruyandex.androidkeyboard.auto
ruyandex.androidkeyboard.tv
ruyandex.blue.market
ruyandex.disk
ruyandex.disk.notificationserviceext
ruyandex.disk.shareext
ruyandex.lavka
ruyandex.mail
ruyandex.mail.notificationserviceextension
ruyandex.market
\ CRYPTA
Vvvv VV Vv VV VV VV vv vv vv vv vv vv ivy
Roe
ru.yandex.mail.notificationserviceextension
ruyandex.market
ruyandex.metro
ruyandex.mobile
ruyandex.mobile.drive
ruyandex.mobile.drive.notification
ruyandex.mobile.keyboard
ru.yandex.mobile.keyboard.extension
ruyandex.mobile.KeyboardExtension
ruyandex.mobile.metro
ruyandex.mobile.music
ruyandex.mobile.music.push-extension
ruyandex.mobile.music.widget-extension
ruyandex.mobile.navigator
ruyandex.mobile.NotificationService
ruyandex.mobile.search
ruyandex.mobile.toloka
ruyandex.mobile.translate
ruyandex.mobile.weather-v2
ruyandex.music
ruyandex.music.samsung
ruyandex.searchplugin
ruyandex.taxi
ruyandex.telemost
ruyandex.traffic
ruyandex.translate
ruyandex.uber
ruyandex.uber-kz
ruyandex.weatherplugin
ru.yandex.yandexmaps
ruyandex yandexnavi
ru.yandex.yandexmaps
ru.yandex.yandexnavi
ru.yandex.ymarket
vvvYv
ru.yandex.ytaxi
Js index.js
~ interests
‘m agro.svg
‘m animals.svg
‘= appliances.svg
‘» beauty.sva
63
```

## Slide 64

#### Ids Associated with Social Media Accounts

64

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ids Associated with Social Media Accounts
web > portal > src > public-info > sections > GraphSection > 45 GraphSection.js
import React, { useEffect, useMemo, useState } from
import { useSelector } from "“react-redux’
react";
import { getPublicGraph, getPublicGraphLoading } from "../../store/selectors";
import { Graph, GraphSkeleton } from "../../components/Graph/Graph"
import { Section } from “../../components/Section/Section";
import { getServicelcon } from "../../icons/services'
import { getAppIcon } from "../../icons/apps";
import "./GraphSection.scss";
import noData from "./no-data.sva";
const IMAGE_SIZE_XS = 12;
const IMAGE_SIZE_S = 31
const IMAGE_SIZE_M = 56;
const IMAGE_SIZE_L = 80;
const NODE_MAPPING = {
email: {
imageSize: IMAGE_SIZEM,
imageHref: "mail",
7
yandexuid: {
imageSize: INAGE_SIZE XS,
imageHref: "yandexuid",
idfa: {
imageSize: INAGE_SIZE_L,
imageHref: "ios",
h
gaid: {
imageSize: IMAGE_SIZE_L,
imageHref: “android”,
he
oaid: {
imageSize: INAGE_SIZE_L,
imageHref: "android",
login: {
imageSize: INAGE_SIZE_M,
imageHref: "key",
h
puid:
imageSize: INAGE_SIZE_M,
imageHref: "key",
he
instagram_login: {
imageSize: IMAGE_SIZE M,
imageHref: "instagram
{
imageSize: IMAGE_SIZEM,
3 GraphSection >
web > portal > src > public-info > sections > GraphSection > 4s GraphSection.js > @ GraphSection > © useEffe:
instagram_id: {
imageSize: IMAGE_SIZE_M,
imageHref: “instagran"
imageSize: IMAGE_SIZE_M,
imageHref: "facebook"
ok_id: {
imageSize: IMAGE_SIZEM,
imageHref: "ok"
imageSize: IMAGE_SIZE_M,
imageHref: "vk"
vk_name: {
imageSize: IMAGE_SIZE M,
imageHref: "vk"
kp_id: {
imageSize: IMAGE_SIZEM,
imageHref: "kinopoisk'
‘uid’
if (item. idType
return { imageHref: item.icon, imageSize: IMAGE_SIZE_S };
return NODE_MAPPING[item. icon] 77 { imageHref: “default, imageSize: IMAGE_SIZE_XS
function getImage(item) {
const disabled = !item.isActive;
if (item, idType *uuid') {
return getAppIcon(item.imageHref, disabled)
scatch(() => getAppIcon("default", disabled) );
return getServiceIcon(item.imageHref, disabled)
scatch(() => getServiceIcon("default", disabled) )
64
```

## Slide 65

## Matcher

65

## Slide 66

#### Matcher

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Matc
ner
\Y matcher
> bin
> bundle
v lib
> config
Y matchers
Vv Vv Vv VM
base_matcher
beeline_matcher
er_telecom_matcher
intentai_matcher
mts_matcher
>
rostelecom_matcher
ya.make
G parser.cpp
C parser.h
66
```

## Slide 67

#### Rostelecom Matcher

67

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rostelecom Matcher
ext_fp > matcher > lib > matchers > rostelecom_matcher > G rostelecom_matcher.cpp
22  TConnection [RostelecomMatcher: :MakeConnection(const TFpEvent& event) {
23 return {
24 «Ip = event.GetIp(),
25 «Port = event.GetPort(),
26 - Timestamp = event.GetUnixtime(),
27 «Domain = NMcDomain: :GetMcDomainForRostelecom(event.GetDuid()),
28 a
29 «}
30
31 void TRostelecomMatcher: :AddConnection(const TFpEvent& event) {
32 auto connection = MakeConnection(event);
33
34 Stats. Count->Add("events. incoming. rostelecom. count") ;
35 Request += TStringBuilder() << connection.Ip << ‘\t'
36 << connection.Port << '\t'
37 << connection.Timestamp << '\t'
38 << connection.Domain << ‘\n';
39 3
40
41 ‘TMatches TRostelecomMatcher::GetMatches() {
42 if (Request. length() ®) {
43 return TMatches();
44 }
45 const auto& requestId = CreateGuidAsString();
46 Log->info("Rostelecom request {} body:\n{}", requestId, Request);
47
48 NNeh::TMessage message(GetApiUrl(), "");
49 Y_ENSURE (NNeh: :NHttp: :MakeFullRequest(message, "", Request, "“text/plain"), "Failed to build request to Rostelecom API");
50
51 Stats. Count->Add("api.calls.rostelecom. count");
52 const auto& resp = MakeRequest(Client, message, TDuration::MilliSeconds(Config.GetApiCallTimeoutMs()), “Rostelecom", requestId, Log);
53
54 return ParseResponse(resp->Data) ;
55 }
56
57 TString TRostelecomMatcher::GetApiUrl() const {
58 return “post://" + Config.GetApiUrl();
67
```

## Slide 68

#### Rostelecom Matcher

68

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rostelecom Matcher
ext_fp > matcher > lib > matchers > rostelecom_matcher > G rostelecom_matcher.cpp
22
23
24
25
26
27
28
29
TConnection [Rostelecomatcher::MakeConnection(const TFpEvent& event) {
el
return {
-Ip = event.GetIp(),
«Port = event.GetPort(),
-Timestamp = event.GetUnixtime(),
-Domain = NMcDomain: :GetMcDomainForRostelecom(event.GetDuid()),
68
```

## Slide 69

#### Rostelecom Matcher

69

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Rostelecom Matcher
41
42
43
44
45
46
47
48
49
58
51
52
55
TMatches TRostelecomMatcher: :GetMatches() {
if (Request. length() == @) {
return TMatches();
}
const auto& requestId = CreateGuidAsString();
Log->info("Rostelecom request {} body:\n{}", requestId, Request);
NNeh::TMessage message(GetApiUrl(), "");
Y_ENSURE (NNeh: :NHttp: :MakeFullRequest(message, "", Request, "text/plain"), "Failed to build request to Rostelecom API")
Stats.Count->Add("api.calls.rostelecom. count");
const auto& resp = MakeRequest(Client, message, TDuration: :MilliSeconds(Config.GetApiCallTimeoutMs()), “Rostelecom", requestId, Log);
return ParseResponse(resp->Data) ;
69
```

## Slide 70

#### Test Result Data

70

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Test Result Data
ext_fp > matcher > bin > test > canondata > {} resultjson > [ ] test_matcher.test_matcher > {} 1
{
"test_matcher.test_matcher": [
{
16999999761000006,
"fake_ertelecom_id_for_5.3.100.0",
‘ext_source": “ertelecom",
100506,
“Logid": 0,
“original_domain"
"port": 5555,
“rtmr_timestamp": 1699999977,
“unixtime": 1699999970,
"user_agent": "Mozilla/5.0 (Windows NT P¥Q)",
é “watchid": 200000000000000006,
“yuid": 1006169999976
"“domain-6.ru",
"duid": 16999999861000016,
2 “ext_id": "mts_id_for_160.1.2.4",
22 “ext_source": “mts",
100516,
+ "160.1.2.4",
"Log_type bs-watch-log",
“original_domain"
"port": 4444,
“rtmr_timestamp": 1699999987,
“unixtime": 1699999970,
"user_agent": "Mozilla/S. (Windows NT
2 “watchid": 200000000000000016,
“yuid": 1016169999986
“domain-16. ru",
“ertelecom",
“hitlogid": 100503,
“ip: "5.3.62.8",
“log type": “bs-watch-log",
"Logid": @,
“original_domain"
"port": 2222,
"rtmr_timestamp": 1699999994,
“unixtime": 1699999990,
4 “user_agent “Mozilla/5.@ (Windows NT
"watchid": 200000000000000003,
“yuid": 1031699999993
“domain-3. ru",
70
```

## Slide 71

# Roadmap

●Background on Yandex Leak ●Dive into code: ○What data Yandex is collecting ○What Yandex is doing with that data ○Who Yandex is sharing that data with ● Conclusions and wrap up

●Q&A

71

## Slide 72

## Conclusion

72

## Slide 73

#### Wrap Up

- ●Yandex has access to a broad international reach of data and it has been evasive about what it can do with that data

●A small amount of data can say a lot when it is matched to entries from a company’s other data sources and analyzed

●Yandex has code to sync some of its data with a Russian-state owned entity

73

## Slide 74

#### Takeaways

●Anonymization is very easily undone when data gets combined with pools from other sources that may contain identifying data

●Pay attention to who runs your SDKs, what data points they collect, and where they send your user data. ●Who gets access to a company’s user data when its assets are sold, the geopolitical climate changes, or a government tightens its control?

74

## Slide 75

## Q&A

Link to Write Up: <u>https://bit.ly/455utBP</u>

75
