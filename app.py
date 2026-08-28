"""Placeholder Streamlit interface for the SchoolShield MVP."""

from __future__ import annotations

import streamlit as st

from schoolshield.config import load_config


def main() -> None:
    """Render the offline SchoolShield foundation page."""
    config = load_config()

    st.set_page_config(
        page_title=config.project_name,
        page_icon="☀️",
        layout="wide",
    )
    st.title(config.project_name)
    st.subheader("School Heat-Resilience Grant Optimizer")
    st.info("Development is in progress. Heat and school data are not loaded yet.")
    st.caption(
        f"Configured for {config.district_display_name} "
        f"(NCES district {config.nces_district_id})."
    )


if __name__ == "__main__":
    main()
