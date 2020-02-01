## Transfer Learning for International Crisis Response

### Challenge

For more information please follow the link [here](https://www.aicrowd.com/challenges/amld-2020-transfer-learning-for-international-crisis-response).

### Resources
The data consists of 4 sets, belonging to 4 organizations (org1 to org4), and each comes with a development set (orgX_dev), and a test set (orgX_test).

The development sets contain the following fields:

`id`: the unique identifier of text snippet; a string value, created by concatenating the name of the organization with a distinct number, for example org1_13005.

`entry_original`: the original text of the snippet, provided in languages, such as English and Spanish.
language: the language of the text snippet.

`entry_translated`: the translation of the text snippet to English, done using Google Translator.

`labels`: the label identifiers of the sectors. Each entry can have several labels. These labels are separated with semicolons (;).

The test sets contain the following fields:

`id`: the unique identifier of text snippet.

`entry_original`: the original text of the snippet.

`language`: the language of the text snippet.

`entry_translated`: the translation of the text snippet to English, done using Google Translator.

***Important:*** As mentioned before, the first three organizations have the same labels, but the fourth has a set of different ones. The sectors regarding each label identifier are provided in the label_captions file. Later in this section, you can find a detailed explanation of the meaning of these sectors, and their potential semantic relations.

### Classes

Humanitarian response is organised in thematic clusters. Clusters are groups of humanitarian organizations, both UN and non-UN, in each of the main sectors of humanitarian action, e.g. water, health and logistics. Those serve as global organizing principle to coordinate humanitarian response.

Sectors for the first, second, and third organization:

(1) Agriculture

(2) Cross: short form of Cross-sectoral; areas of humanitarian response that require action in more than one sector. For example malnutrition requires humanitarian interventions in health, access to food, access to basic hygiene items and clean water, and access to non-food items such as bottles to feed infants.

(3) Education

(4) Food

(5) Health

(6) Livelihood: Access to employment and income

(7) Logistics: Any logistical support needed to carry out humanitarian activities e.g. air transport, satellite phone connection etc.

(8) NFI: Non-food items needed in daily life that are not food such as bedding, mattrassess, jerrycans, coal or oil for heating

(9) Nutrition

(10) Protection

(11) Shelter

(12) WASH (Water, Sanitation and Hygiene)

Sectors for the fourth organization:

(101) Child Protection

(102) Early Recovery and Livelihoods

(103) Education

(104) Food

(105) GBV: Gender Based Violence

(106) Health

(107) Logistics

(108) Mine Action

(109) Nutrition

(110) Protection

(111) Shelter and NFIs

(112) WASH
