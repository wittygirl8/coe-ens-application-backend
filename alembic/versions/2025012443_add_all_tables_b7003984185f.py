"""add all tables

Revision ID: b7003984185f
Revises: 342350439476
Create Date: 2025-01-24 10:43:00.878558

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "b7003984185f"
down_revision = "342350439476"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cyes",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "external_supplier_data",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("country", sa.String(length=20), nullable=True),
        sa.Column("location", sa.String(length=30), nullable=True),
        sa.Column("address", sa.Text(), nullable=True),
        sa.Column("is_active", sa.String(length=15), nullable=True),
        sa.Column("operation_type", sa.String(length=50), nullable=True),
        sa.Column("legal_form", sa.String(length=50), nullable=True),
        sa.Column("bvd_id", sa.String(length=50), nullable=True),
        sa.Column("national_identifier_type", sa.String(length=50), nullable=True),
        sa.Column("national_identifier", sa.String(length=50), nullable=True),
        sa.Column("alias", sa.Text(), nullable=True),
        sa.Column("incorporation_date", sa.Date(), nullable=True),
        sa.Column("num_subsidiaries", sa.Integer(), nullable=True),
        sa.Column("num_companies_in_corp_grp", sa.Integer(), nullable=True),
        sa.Column("num_direct_shareholders", sa.Integer(), nullable=True),
        sa.Column(
            "operating_revenue", sa.Numeric(precision=18, scale=2), nullable=True
        ),
        sa.Column(
            "profit_loss_after_tax", sa.Numeric(precision=18, scale=2), nullable=True
        ),
        sa.Column(
            "debt_to_equity_ratio", sa.Numeric(precision=10, scale=4), nullable=True
        ),
        sa.Column("ebitda", sa.Numeric(precision=18, scale=2), nullable=True),
        sa.Column("current_ratio", sa.Numeric(precision=10, scale=4), nullable=True),
        sa.Column(
            "roe_using_net_income", sa.Numeric(precision=10, scale=4), nullable=True
        ),
        sa.Column("pl_date", sa.Date(), nullable=True),
        sa.Column("pr_qualitative_score", sa.String(length=1), nullable=True),
        sa.Column("pr_more_risk_score", sa.String(length=3), nullable=True),
        sa.Column("pr_reactive_more_risk_score", sa.String(length=3), nullable=True),
        sa.Column("pr_qualitative_score_date", sa.Date(), nullable=True),
        sa.Column("pr_more_risk_score_date", sa.Date(), nullable=True),
        sa.Column("pr_reactive_more_risk_score_date", sa.Date(), nullable=True),
        sa.Column(
            "payment_risk_score", sa.Numeric(precision=4, scale=2), nullable=True
        ),
        sa.Column("event", sa.JSON(), nullable=True),
        sa.Column(
            "esg_overall_rating", sa.Numeric(precision=3, scale=2), nullable=True
        ),
        sa.Column(
            "esg_environmental_rating", sa.Numeric(precision=3, scale=2), nullable=True
        ),
        sa.Column("esg_social_rating", sa.Numeric(precision=5, scale=2), nullable=True),
        sa.Column(
            "esg_governance_rating", sa.Numeric(precision=3, scale=2), nullable=True
        ),
        sa.Column("esg_date", sa.Date(), nullable=True),
        sa.Column("cyber_risk_score", sa.Numeric(precision=4, scale=2), nullable=True),
        sa.Column("cyber_botnet_infection", sa.String(length=1), nullable=True),
        sa.Column("cyber_malware_servers", sa.String(length=1), nullable=True),
        sa.Column("cyber_ssl_certificate", sa.String(length=1), nullable=True),
        sa.Column("cyber_webpage_headers", sa.String(length=1), nullable=True),
        sa.Column("cyber_date", sa.Date(), nullable=True),
        sa.Column("implied_cyber_risk_score", sa.Text(), nullable=True),
        sa.Column("implied_cyber_risk_score_date", sa.Date(), nullable=True),
        sa.Column("beneficial_owners", sa.JSON(), nullable=True),
        sa.Column("global_ultimate_owner", sa.JSON(), nullable=True),
        sa.Column("shareholders", sa.JSON(), nullable=True),
        sa.Column("ultimately_owned_subsidiaries", sa.JSON(), nullable=True),
        sa.Column("ultimate_beneficiary_owner", sa.JSON(), nullable=True),
        sa.Column("other_ultimate_beneficiary", sa.JSON(), nullable=True),
        sa.Column("ens_id", sa.String(length=100), nullable=True),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "fstb",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "kpi_master_data",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "lgrk",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "oval",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "ovar",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "rfct",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "sape",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "sown",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kpi_area", sa.String(), nullable=False),
        sa.Column("kpi_code", sa.String(), nullable=False),
        sa.Column("kpi_flag", sa.Boolean(), nullable=False),
        sa.Column("kpi_value", sa.String(), nullable=True),
        sa.Column("kpi_details", sa.String(), nullable=True),
        sa.Column("ens_id", sa.String(), nullable=False),
        sa.Column("session_id", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "supplier_master_data",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("name_international", sa.String(length=255), nullable=True),
        sa.Column("address", sa.Text(), nullable=True),
        sa.Column("postcode", sa.String(length=20), nullable=True),
        sa.Column("city", sa.String(length=100), nullable=True),
        sa.Column("country", sa.String(length=100), nullable=True),
        sa.Column("phone_or_fax", sa.String(length=50), nullable=True),
        sa.Column("email_or_website", sa.String(length=100), nullable=True),
        sa.Column("national_id", sa.String(length=50), nullable=True),
        sa.Column("state", sa.String(length=100), nullable=True),
        sa.Column("ens_id", sa.String(length=50), nullable=True),
        sa.Column("session_id", sa.String(length=50), nullable=False),
        sa.Column("bvd_id", sa.String(length=50), nullable=True),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("verified", sa.Boolean(), nullable=False),
        sa.Column("otp", sa.String(), nullable=True),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_table_email"), "users_table", ["email"], unique=True)
    op.create_index(op.f("ix_users_table_id"), "users_table", ["id"], unique=False)
    op.create_index(
        op.f("ix_users_table_user_id"), "users_table", ["user_id"], unique=True
    )
    op.create_index(
        op.f("ix_users_table_username"), "users_table", ["username"], unique=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_table_username"), table_name="users_table")
    op.drop_index(op.f("ix_users_table_user_id"), table_name="users_table")
    op.drop_index(op.f("ix_users_table_id"), table_name="users_table")
    op.drop_index(op.f("ix_users_table_email"), table_name="users_table")
    op.drop_table("users_table")
    op.drop_table("supplier_master_data")
    op.drop_table("sown")
    op.drop_table("sape")
    op.drop_table("rfct")
    op.drop_table("ovar")
    op.drop_table("oval")
    op.drop_table("news")
    op.drop_table("lgrk")
    op.drop_table("kpi_master_data")
    op.drop_table("fstb")
    op.drop_table("external_supplier_data")
    op.drop_table("cyes")
    # ### end Alembic commands ###
