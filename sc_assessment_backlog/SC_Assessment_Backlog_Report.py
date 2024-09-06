import connections.SQL as SQL
import pandas as pd
from SC_Assessment_Backlog_SQL import QUERY as Q1
from SC_Assessment_Backlog_Other_SQL import QUERY as Q2
import time

#Creates tables from the DataFrame that counts the number of unique resources in a column, both in the entire DataFrame and grouped by Repository.
def summarize():
    rep_count = (df.repository.value_counts()).reset_index()

    conserv_count = (df.conservation_issues.fillna('None').str.get_dummies(sep='; ').sum()).reset_index()
    conserv_count.columns = ["conservation_issues", "count"]
    consplit = df.assign(conservation_issues=df['conservation_issues'].fillna('None').str.split('; ')).explode('conservation_issues')
    conserv_rep_count = (consplit.groupby('repository')['conservation_issues'].value_counts()).reset_index()

    format_count = (df.formats.fillna('None').str.get_dummies(sep='; ').sum()).reset_index()
    format_count.columns = ["formats", "count"]
    formsplit = df.assign(formats=df['formats'].fillna('None').str.split('; ')).explode('formats')
    format_rep_count = (formsplit.groupby('repository')['formats'].value_counts()).reset_index()

    extent_count = (df.extent_value.fillna('None').str.get_dummies(sep='; ').sum()).reset_index()
    extent_count.columns = ["extent_value", "count"]
    extsplit = df.assign(extent_value=df['extent_value'].fillna('None').str.split('; ')).explode('extent_value')
    extent_rep_count = (extsplit.groupby('repository')['extent_value'].value_counts()).reset_index()
  
    def count_yes(column):
        return (column == 'yes').sum()

  #Creates a summary of the number of the number of assessments with specific boxes checked by repository.
    existing_description = df[['accession_report', 'appraisal', 'container_list', 'catalog_record', 'control_file', 'finding_aid_ead', 'finding_aid_paper', 'finding_aid_word', 'finding_aid_spreadsheet', 'review_required', 'sensitive_material', 'deed_of_gift', 'finding_aid_online', 'related_eac_record', 'inactive']].apply(count_yes).reset_index()
    existing_description.columns = ["existing_description", "count"]
    existing_description_rep = df.groupby('repository').agg(
    accession_report=('accession_report', count_yes),
    appraisal=('appraisal', count_yes),
    container_list=('container_list', count_yes),
    catalog_record=('catalog_record', count_yes),
    control_file=('control_file', count_yes),
    finding_aid_ead=('finding_aid_ead', count_yes),
    finding_aid_paper=('finding_aid_paper', count_yes),
    finding_aid_word=('finding_aid_word', count_yes),
    finding_aid_spreadsheet=('finding_aid_spreadsheet', count_yes),
    review_required=('review_required', count_yes),
    sensitive_material=('sensitive_material', count_yes),
    deed_of_gift=('deed_of_gift', count_yes),
    finding_aid_online=('finding_aid_online', count_yes),
    related_eac_record=('related_eac_record', count_yes),
    inactive=('inactive', count_yes)).reset_index()

  #Count of the number of assessments whose Research value is 7 or above, but whose Access rating is 3 or lower.
    low_int_access = pd.DataFrame({'Number of resources with high research value and low intellectual access' : [df[(pd.to_numeric(df['research_value_quality_rating']) > 6) & (pd.to_numeric(df['intellectual_access_quality_rating']) < 4)].shape[0]]})
    low_phy_access = pd.DataFrame({'Number of resources with high research value and low physical access' : [df[(pd.to_numeric(df['research_value_quality_rating']) > 6) & (pd.to_numeric(df['physical_access_quality_rating']) < 4)].shape[0]]})

    #write everything to an excel file with their own sheet.
    with pd.ExcelWriter(file_name, engine='xlsxwriter', mode='w') as writer:
        df.to_excel(writer, sheet_name="Data", index=False)
        rep_count.to_excel(writer, sheet_name='Repositories Count', index=False)
        conserv_count.to_excel(writer, sheet_name='Total Conservation Issues', index=False)
        conserv_rep_count.to_excel(writer, sheet_name='Conservation by Repository', index=False)
        format_count.to_excel(writer, sheet_name='Total Formats', index=False)
        format_rep_count.to_excel(writer, sheet_name='Total Formats by Repository', index=False)
        extent_count.to_excel(writer, sheet_name='Total Extents', index=False)
        extent_rep_count.to_excel(writer, sheet_name='Total Extents by Repository', index=False)
        existing_description.to_excel(writer, sheet_name='Total Existing Descriptions', index=False)
        existing_description_rep.to_excel(writer, sheet_name='Total Descs by Repository', index=False)
        low_int_access.to_excel(writer, sheet_name='Low Intellectual Access', index=False)
        low_phy_access.to_excel(writer, sheet_name='Low Physical Access', index=False)

#Check is the SQL connection is successful, if not it returns and error. Pulls the function from a seperate file not included that contains passwords and username information.
if SQL.conn():
    print("Connection Successful!")
    cursor = SQL.connection.cursor()

  #Pulls the Query from SC_Assessment_Backlog_SQL.py file and creates an excel file with today's date containing the raw data and the summary sheets.
    cursor.execute(Q1)
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=["URI", "repository", "identifier", "title", "extent_value", "assessment_purpose", "survey_begin", "survy_end", "scope", "surveyed_duration", "surveyed_extent", "accession_report", "appraisal", "container_list", "catalog_record", "control_file", "finding_aid_ead", "finding_aid_paper", "finding_aid_word", "finding_aid_spreadsheet", "review_required", "sensitive_material", "deed_of_gift", "finding_aid_online", "related_eac_record", "inactive", "conservation_note", "description_notes", "general_assessment_note", "special_format_note", "exhibition_value_note", "review_note", "monetary_value", "monetary_value_note", "assessment_attribute_notes", "documentation_quality_rating", "housing_quality_rating", "intellectual_access_quality_rating", "interest_quality_rating", "physical_access_quality_rating", "physical_condition_quality_rating", "reformatting_readiness_quality_rating", "research_value_quality_rating", "formats", "conservation_issues"])
    date_str = time.strftime("%y%m%d")
    file_name = f'files/{date_str}_SC_Assessment_Backlog_all.xlsx'
    summarize()

  #Pulls the Query from SC_Assessment_Backlog_Other_SQL.py file and creates an excel file with today's date containing the raw data and the summary sheets.
    cursor.execute(Q2)
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=["URI", "repository", "identifier", "title", "extent_value", "assessment_purpose", "survey_begin", "survy_end", "scope", "surveyed_duration", "surveyed_extent", "accession_report", "appraisal", "container_list", "catalog_record", "control_file", "finding_aid_ead", "finding_aid_paper", "finding_aid_word", "finding_aid_spreadsheet", "review_required", "sensitive_material", "deed_of_gift", "finding_aid_online", "related_eac_record", "inactive", "conservation_note", "description_notes", "general_assessment_note", "special_format_note", "exhibition_value_note", "review_note", "monetary_value", "monetary_value_note", "assessment_attribute_notes", "documentation_quality_rating", "housing_quality_rating", "intellectual_access_quality_rating", "interest_quality_rating", "physical_access_quality_rating", "physical_condition_quality_rating", "reformatting_readiness_quality_rating", "research_value_quality_rating", "formats", "conservation_issues"])
    file_name = f'files/{date_str}_SC_Assessment_Backlog_other.xlsx'
    summarize()
else:
    print("Connection Failed. Are you connected to the VPN?")
