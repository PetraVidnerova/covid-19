skript na stahování migračních dat z https://www.inovujemesdaty.cz/

matice jsou v https://github.com/vit-tucek/covid-19/blob/master/locdata/matrices.zip
stažená data v https://github.com/vit-tucek/covid-19/blob/master/locdata/commuting_relations.zip

číselník lokalit: http://api.inovujemesdaty.cz/locations.csv

počty obyvatel ve správních obvodech obcí s rozšířenou působností k 1.1.2019 z https://www.czso.cz/csu/czso/pocet-obyvatel-v-obcich-za0wri436p (do ORP bylo nutno ručně přidat Prahu) je v population.csv spolu se sloupcem id mapujícím na číselník lokalit (pouze ORP)

Distanční matice má ve sloupcích dojezdy z i-tého města. Indexace dle abecedy, to jest tak, jak je to v population.csv. Podtržítko následované s číslem jsou data za měsíc, tak, jak je vrací https://www.inovujemesdaty.cz/commuting-relations a tedy matice jsou celočíselné. Podtržítko Q2 obsahuje jednoduchý průměr (bez zohlednění počtu dnů) za druhé čtvrtletí. 
