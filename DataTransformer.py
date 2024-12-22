from datetime import datetime
from typing import List, Dict


class DataTransformer:
    def __init__(self, data: List[Dict]):
        self.data = data

    def process_candidates(self):
        processed_candidates = []
        for candidate in self.data:
            name = candidate.get("contact_info", {}).get("name", {}).get("formatted_name")
            experiences = candidate.get("experience", [])
            processed_experiences = self._process_experiences(experiences)

            candidate_summary = {
                "name": name,
                "experiences": processed_experiences
            }
            processed_candidates.append(candidate_summary)
        return processed_candidates

    def _process_experiences(self, experiences: List[Dict]):
        processed_experiences = []

        if not experiences:
            processed_experiences.append({
                "title": "No Experience Found",
                "from": "",
                "to": "",
                "location": "",
                "gap_days": 0
            })
            return processed_experiences

        experiences.sort(key=lambda x: datetime.strptime(x["start_date"], "%b/%d/%Y"))

        for i in range(len(experiences)):
            exp = experiences[i]

            processed_experiences.append({
                "title": exp.get("title", "Unknown"),
                "from": exp.get("start_date", ""),
                "to": exp.get("end_date", ""),
                "location": exp.get("location", {}).get("short_display_address", "Unknown")
            })

            if i > 0:
                prev_end_date_str = experiences[i - 1].get("end_date")
                current_start_date_str = exp.get("start_date")

                if prev_end_date_str and current_start_date_str:
                    try:
                        prev_end_date = datetime.strptime(prev_end_date_str, "%b/%d/%Y")
                        current_start_date = datetime.strptime(current_start_date_str, "%b/%d/%Y")

                        gap_days = (current_start_date - prev_end_date).days
                        if gap_days > 1:
                            processed_experiences.insert(i, {
                                "title": "Gap in CV",
                                "from": prev_end_date_str,
                                "to": current_start_date_str,
                                "location": "",
                                "gap_days": gap_days
                            })
                    except ValueError:
                        continue

        return processed_experiences
