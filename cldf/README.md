<a name="ds-genericmetadatajson"> </a>

# Generic Glottography dataset derived from Walker and Ribeiro 2011 "Bayesian Phylogeography of the Arawak Expansion in Lowland South America"

**CLDF Metadata**: [Generic-metadata.json](./Generic-metadata.json)

**Sources**: [sources.bib](./sources.bib)

This dataset provides contemporary, non-overlapping speaker areas for Arawakan languages derived from figure S1 in the supplementary material for Walker & Ribeiro 2011. Languages for which only point locations are given in the source are omitted.

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Walker, Robert S. & Lincoln A. Ribeiro. 2011. Bayesian Phylogeography of the Arawak Expansion in Lowland South America. 278(1718). 2562–2567. doi: 10.1098/rspb.2010.2579. Royal Society.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dc:spatial](http://purl.org/dc/terms/spatial) | westlimit=-75.9; southlimit=-22.3; eastlimit=-50.1; northlimit=12.5
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/Glottography/walker2011bayesian
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/Glottography/walker2011bayesian/tree/bec35d8">Glottography/walker2011bayesian bec35d8</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.1">Glottolog v5.1</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.12.3</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | walker2011bayesian
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-mediacsv"></a>Table [media.csv](./media.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF MediaTable](http://cldf.clld.org/v1.0/terms.rdf#MediaTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Media_Type](http://cldf.clld.org/v1.0/terms.rdf#mediaType) | `string`<br>Regex: `[^/]+/.+` | 
[Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl) | `anyURI` | 
[Path_In_Zip](http://cldf.clld.org/v1.0/terms.rdf#pathInZip) | `string` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 31


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal`<br>&ge; -90<br>&le; 90 | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal`<br>&ge; -180<br>&le; 180 | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string`<br>Regex: `[a-z]{3}` | 
[Feature_IDs](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | list of `string` (separated by ` `) | List of identifiers of features that were aggregated to create the feature referenced by Speaker_Area.<br>References [contributions.csv::ID](#table-contributionscsv)
`Glottolog_Languoid_Level` | `string`<br>Valid choices:<br> `dialect` `language` `family` | https://glottolog.org/meta/glossary#Languoid
`Family` | `string` | Name of the top-level family for the languoid in the Glottolog classification. A null value in this column marks 1) top-level families in case Glottolog_Languoid_Level is 'family' and 2) isolates in case Glottolog_Languoid_Level is 'language'.
[Speaker_Area](http://cldf.clld.org/v1.0/terms.rdf#speakerArea) | `string` | References [media.csv::ID](#table-mediacsv)

## <a name="table-contributionscsv"></a>Table [contributions.csv](./contributions.csv)

We list the individual features from the source dataset as contributions in order to preserve the original metadata and a point of reference for the aggregated shapes.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable)
[dc:extent](http://purl.org/dc/terms/extent) | 30


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Contributor](http://cldf.clld.org/v1.0/terms.rdf#contributor) | `string` | 
[Citation](http://cldf.clld.org/v1.0/terms.rdf#citation) | `string` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | References a Glottolog languoid most closely matching the linguistic entity described by the feature.
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
[Media_ID](http://cldf.clld.org/v1.0/terms.rdf#mediaReference) | `string` | Features are linked to GeoJSON files that store the geo data.<br>References [media.csv::ID](#table-mediacsv)
`Map_Name` | `string` | Name of the map as given in the source publication.

