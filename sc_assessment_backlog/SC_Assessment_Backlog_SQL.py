QUERY = ('''
        SELECT DISTINCT CONCAT('/repositories/', resource.repo_id, '/resources/', resource.id) as uri
	, repository.name as repository
	, JSON_UNQUOTE(JSON_EXTRACT(resource.identifier, '$[0]')) as identifier
	, resource.title
	, extents.extent_value
	, assessment.purpose
	, assessment.survey_begin
	, assessment.survey_end
	, assessment.scope
	, assessment.surveyed_duration
	, assessment.surveyed_extent
	, IF(assessment.accession_report = 1, 'yes', 'no') as accession_report
	, IF(assessment.appraisal = 1, 'yes', 'no') as appraisal
	, IF(assessment.container_list = 1, 'yes', 'no') as container_list
	, IF(assessment.catalog_record = 1, 'yes', 'no') as catalog_record
	, IF(assessment.control_file = 1, 'yes', 'no') as control_file
	, IF(assessment.finding_aid_ead = 1, 'yes', 'no') as finding_aid_ead
	, IF(assessment.finding_aid_paper = 1, 'yes', 'no') as finding_aid_paper
	, IF(assessment.finding_aid_word = 1, 'yes', 'no') as finding_aid_word
	, IF(assessment.finding_aid_spreadsheet = 1, 'yes', 'no') as finding_aid_spreadsheet
	, IF(assessment.review_required = 1, 'yes', 'no') as review_required
	, IF(assessment.sensitive_material = 1, 'yes', 'no') as sensitive_material
	, IF(assessment.deed_of_gift = 1, 'yes', 'no') as deed_of_gift
	, IF(assessment.finding_aid_online = 1, 'yes', 'no') as finding_aid_online
	, IF(assessment.related_eac_records = 1, 'yes', 'no') as related_eac_record
	, IF(assessment.inactive = 1, 'yes', 'no') as inactive
	, assessment.conservation_note
	, assessment.existing_description_notes
	, assessment.general_assessment_note
	, assessment.special_format_note
	, assessment.exhibition_value_note
	, assessment.review_note
	, assessment.monetary_value
	, assessment.monetary_value_note
	, aans.notes as assessment_attribute_notes
	, ratings.documentation_quality_rating
	, ratings.housing_quality_rating
	, ratings.intellectual_access_quality_rating
	, ratings.interest_quality_rating
	, ratings.physical_access_quality_rating
	, ratings.physical_condition_quality_rating
	, ratings.reformatting_readiness_quality_rating
	, ratings.research_value_quality_rating
	, formats.formats
	, issues.conservation_issues
FROM assessment
JOIN assessment_rlshp ar on ar.assessment_id = assessment.id
LEFT JOIN (SELECT aan.assessment_id as assess_id
					, GROUP_CONCAT(aan.note SEPARATOR '; ') as notes
					FROM assessment_attribute_note aan
					GROUP BY aan.assessment_id) aans on aans.assess_id = assessment.id
JOIN resource on ar.resource_id = resource.id
JOIN repository on resource.repo_id = repository.id
LEFT JOIN (SELECT GROUP_CONCAT(CONCAT(extent.number, ' ', ev.value) SEPARATOR '; ') as extent_value
			 , resource.id as re_id
			FROM extent
			LEFT JOIN enumeration_value ev on ev.id = extent.extent_type_id
			JOIN resource on resource.id = extent.resource_id
			GROUP BY resource.id) extents on resource.id = extents.re_id
LEFT JOIN (SELECT aa.assessment_id as assess_id
			, MAX(CASE WHEN aad.label = 'Documentation Quality' THEN aa.value ELSE NULL END) as documentation_quality_rating
			, MAX(CASE WHEN aad.label = 'Housing Quality' THEN aa.value ELSE NULL END) as housing_quality_rating
			, MAX(CASE WHEN aad.label = 'Intellectual Access (description)' THEN aa.value ELSE NULL END) as intellectual_access_quality_rating
			, MAX(CASE WHEN aad.label = 'Interest' THEN aa.value ELSE NULL END) as interest_quality_rating
			, MAX(CASE WHEN aad.label = 'Physical Access (arrangement)' THEN aa.value ELSE NULL END) as physical_access_quality_rating
			, MAX(CASE WHEN aad.label = 'Physical Condition' THEN aa.value ELSE NULL END) as physical_condition_quality_rating
			, MAX(CASE WHEN aad.label = 'Reformatting Readiness' THEN aa.value ELSE NULL END) as reformatting_readiness_quality_rating
			, MAX(CASE WHEN aad.label = 'Research Value' THEN aa.value ELSE NULL END) as research_value_quality_rating
		FROM assessment_attribute aa
		LEFT JOIN assessment_attribute_definition aad on aad.id = aa.assessment_attribute_definition_id
		WHERE aad.type = 'rating'
		GROUP BY aa.assessment_id) as ratings on ratings.assess_id = assessment.id
LEFT JOIN (SELECT aa.assessment_id as assess_id 
			, GROUP_CONCAT(aad.label SEPARATOR '; ') as formats
		FROM assessment_attribute aa
		LEFT JOIN assessment_attribute_definition aad on aad.id = aa.assessment_attribute_definition_id
		WHERE aad.type = 'format'
		GROUP BY aa.assessment_id) as formats on formats.assess_id = assessment.id
LEFT JOIN (SELECT aa.assessment_id as assess_id 
			, GROUP_CONCAT(aad.label SEPARATOR '; ') as conservation_issues
		FROM assessment_attribute aa
		LEFT JOIN assessment_attribute_definition aad on aad.id = aa.assessment_attribute_definition_id
		WHERE aad.type = 'conservation_issue'
		GROUP BY aa.assessment_id) as issues on issues.assess_id = assessment.id
WHERE purpose like '%backlog%'
UNION ALL
SELECT DISTINCT CONCAT('/repositories/', accession.repo_id, '/accessions/', accession.id) as uri
	, repository.name as repository
	, CONCAT(JSON_UNQUOTE(JSON_EXTRACT(accession.identifier, '$[0]')),
				'-',
		     JSON_UNQUOTE(JSON_EXTRACT(accession.identifier, '$[1]')),
		     	'-',
		     JSON_UNQUOTE(JSON_EXTRACT(accession.identifier, '$[2]'))) as identifier
	, accession.title
	, extents.extent_value
	, assessment.purpose
	, assessment.survey_begin
	, assessment.survey_end
	, assessment.scope
	, assessment.surveyed_duration
	, assessment.surveyed_extent
	, IF(assessment.accession_report = 1, 'yes', 'no') as accession_report
	, IF(assessment.appraisal = 1, 'yes', 'no') as appraisal
	, IF(assessment.container_list = 1, 'yes', 'no') as container_list
	, IF(assessment.catalog_record = 1, 'yes', 'no') as catalog_record
	, IF(assessment.control_file = 1, 'yes', 'no') as control_file
	, IF(assessment.finding_aid_ead = 1, 'yes', 'no') as finding_aid_ead
	, IF(assessment.finding_aid_paper = 1, 'yes', 'no') as finding_aid_paper
	, IF(assessment.finding_aid_word = 1, 'yes', 'no') as finding_aid_word
	, IF(assessment.finding_aid_spreadsheet = 1, 'yes', 'no') as finding_aid_spreadsheet
	, IF(assessment.review_required = 1, 'yes', 'no') as review_required
	, IF(assessment.sensitive_material = 1, 'yes', 'no') as sensitive_material
	, IF(assessment.deed_of_gift = 1, 'yes', 'no') as deed_of_gift
	, IF(assessment.finding_aid_online = 1, 'yes', 'no') as finding_aid_online
	, IF(assessment.related_eac_records = 1, 'yes', 'no') as related_eac_record
	, IF(assessment.inactive = 1, 'yes', 'no') as inactive
	, assessment.conservation_note
	, assessment.existing_description_notes
	, assessment.general_assessment_note
	, assessment.special_format_note
	, assessment.exhibition_value_note
	, assessment.review_note
	, assessment.monetary_value
	, assessment.monetary_value_note
	, aans.notes as assessment_attribute_notes
	, ratings.documentation_quality_rating
	, ratings.housing_quality_rating
	, ratings.intellectual_access_quality_rating
	, ratings.interest_quality_rating
	, ratings.physical_access_quality_rating
	, ratings.physical_condition_quality_rating
	, ratings.reformatting_readiness_quality_rating
	, ratings.research_value_quality_rating
	, formats.formats
	, issues.conservation_issues
FROM assessment
JOIN assessment_rlshp ar on ar.assessment_id = assessment.id
LEFT JOIN (SELECT aan.assessment_id as assess_id
					, GROUP_CONCAT(aan.note SEPARATOR '; ') as notes
					FROM assessment_attribute_note aan
					GROUP BY aan.assessment_id) aans on aans.assess_id = assessment.id
JOIN accession on ar.accession_id = accession.id
JOIN repository on accession.repo_id = repository.id
LEFT JOIN (SELECT GROUP_CONCAT(CONCAT(extent.number, ' ', ev.value) SEPARATOR '; ') as extent_value
			, accession.id as acc_id
			FROM extent
			LEFT JOIN enumeration_value ev on ev.id = extent.extent_type_id
			JOIN accession on accession.id = extent.accession_id
			GROUP BY accession.id) extents on accession.id = extents.acc_id
LEFT JOIN (SELECT aa.assessment_id as assess_id
			, MAX(CASE WHEN aad.label = 'Documentation Quality' THEN aa.value ELSE NULL END) as documentation_quality_rating
			, MAX(CASE WHEN aad.label = 'Housing Quality' THEN aa.value ELSE NULL END) as housing_quality_rating
			, MAX(CASE WHEN aad.label = 'Intellectual Access (description)' THEN aa.value ELSE NULL END) as intellectual_access_quality_rating
			, MAX(CASE WHEN aad.label = 'Interest' THEN aa.value ELSE NULL END) as interest_quality_rating
			, MAX(CASE WHEN aad.label = 'Physical Access (arrangement)' THEN aa.value ELSE NULL END) as physical_access_quality_rating
			, MAX(CASE WHEN aad.label = 'Physical Condition' THEN aa.value ELSE NULL END) as physical_condition_quality_rating
			, MAX(CASE WHEN aad.label = 'Reformatting Readiness' THEN aa.value ELSE NULL END) as reformatting_readiness_quality_rating
			, MAX(CASE WHEN aad.label = 'Research Value' THEN aa.value ELSE NULL END) as research_value_quality_rating
		FROM assessment_attribute aa
		LEFT JOIN assessment_attribute_definition aad on aad.id = aa.assessment_attribute_definition_id
		WHERE aad.type = 'rating'
		GROUP BY aa.assessment_id) as ratings on ratings.assess_id = assessment.id
LEFT JOIN (SELECT aa.assessment_id as assess_id 
			, GROUP_CONCAT(aad.label SEPARATOR '; ') as formats
		FROM assessment_attribute aa
		LEFT JOIN assessment_attribute_definition aad on aad.id = aa.assessment_attribute_definition_id
		WHERE aad.type = 'format'
		GROUP BY aa.assessment_id) as formats on formats.assess_id = assessment.id
LEFT JOIN (SELECT aa.assessment_id as assess_id 
			, GROUP_CONCAT(aad.label SEPARATOR '; ') as conservation_issues
		FROM assessment_attribute aa
		LEFT JOIN assessment_attribute_definition aad on aad.id = aa.assessment_attribute_definition_id
		WHERE aad.type = 'conservation_issue'
		GROUP BY aa.assessment_id) as issues on issues.assess_id = assessment.id
LEFT JOIN extent on extent.accession_id = accession.id
LEFT JOIN enumeration_value ev on ev.id = extent.extent_type_id
WHERE purpose like '%backlog%'
         ''')
