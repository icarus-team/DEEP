import pandas as pd
import numpy as np


ROUND_POINT = 4


class SubmissionError(Exception):
    pass


class DeepEvaluator:
    def __init__(self, answer_filenames, round=1):
        """
        `round` : Holds the round for which the evaluation is being done.
        can be 1, 2...upto the number of rounds the challenge has.
        Different rounds will mostly have different ground truth files.
        """
        self.orgs = [x.split('_')[0] for x in answer_files]
        self.answer_filenames = answer_filenames
        self.org_scores = {x: 0 for x in self.orgs}  # Initialize all orgs score to zero
        self.org_entries_size = dict()
        self._answers = None  # This will contain dictionary as  { <entry_id> : set(entry_labels) }
        self.round = round

    @property
    def answers(self):
        """Read answers from answer file paths and accumulate them to a single dictionary"""
        if self._answers is None:
            self._answers = {}
            for org, filename in zip(self.orgs, self.answer_filenames):
                answer_path = f'data/{filename}.csv'
                answer_df = pd.read_csv(answer_path)
                self.org_entries_size[org] = len(answer_df)
                for index, row in answer_df.iterrows():
                    str_labels = str(row['labels'])
                    labels = [int(x) for x in str_labels.split(';') if x]
                    self._answers[row['id']] = set(labels)
        return self._answers

    def _validate_submission(self, submission_file_path):
        submission_df = pd.read_csv(submission_file_path)
        # check if length of submission equals all the rows in reference files
        if not len(submission_df) == len(self.answers.keys()):
            raise SubmissionError('Submission row counts mismatch!!')

        # TODO: add other validations
        return submission_df

    def _evaluate(self, client_payload, _context={}):
        """
        `client_payload` will be a dict with (atleast) the following keys :
        - submission_file_path : local file path of the submitted file
        - aicrowd_submission_id : A unique id representing the submission
        - aicrowd_participant_id : A unique id for participant/team submitting (if enabled)
        """
        submission_file_path = client_payload["submission_file_path"]
        aicrowd_submission_id = client_payload["aicrowd_submission_id"]
        aicrowd_participant_uid = client_payload["aicrowd_participant_id"]

        submission = self._validate_submission(submission_file_path)
        # Or your preferred way to read your submission

        for index, row in submission.iterrows():
            rowid = row['id']
            org, enryid = rowid.split('_')
            if org not in self.org_scores:
                raise SubmissionError(f'Invalid submission entry. No entry with id {rowid}.')
            prediction = int(row['predicted_label'])
            actual_labels = self.answers.get(rowid, set())
            if prediction in actual_labels:
                self.org_scores[org] += 1

        return self.calculate_final_scores()

    def calculate_final_scores(self):
        org_scores = {}
        for org, score in self.org_scores.items():
            orgscore = round(score / self.org_entries_size[org], ROUND_POINT)
            org_scores[org] = orgscore

        # Secondary Score is just the inverse of standard deviation
        # TODO: have a better secondary score metric
        org_scores_list = list(org_scores.values())
        return {
            "meta": {
                **{
                    f'score_{org}': score for (org, score) in org_scores.items()
                }
            },
            "score": round(np.mean(org_scores_list), ROUND_POINT),
            # "score_secondary": round(
                # 1.0 / (2 + np.std(org_scores_list)),  # 2 is just arbitrary
                # ROUND_POINT
            # ),
        }


if __name__ == "__main__":
    # Lets assume the the ground_truth is a CSV file
    # and is present at data/ground_truth.csv
    # and a sample submission is present at data/sample_submission.csv
    answer_files = [
        'org1_reference_test',
        'org2_reference_test',
        'org3_reference_test',
        'org4_reference_test'
    ]

    _client_payload = {}
    _client_payload["submission_file_path"] = "data/sample_submission.csv"
    _client_payload["aicrowd_submission_id"] = 1123
    _client_payload["aicrowd_participant_id"] = 1234

    # Instaiate a dummy context
    _context = {}
    # Instantiate an evaluator
    aicrowd_evaluator = DeepEvaluator(answer_files)
    # Evaluate
    result = aicrowd_evaluator._evaluate(_client_payload, _context)
    print(result)
