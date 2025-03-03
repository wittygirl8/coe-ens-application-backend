"""update supplier_master_data

Revision ID: 034e432ba480
Revises: 4c9b4f28afca
Create Date: 2025-01-28 16:13:19.057500

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "034e432ba480"
down_revision = "4c9b4f28afca"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("matchbvdid")
    op.drop_table("orgdata")
    # Check if the column already exists before trying to add it
    conn = op.get_bind()
    result = conn.execute(sa.text("""
        SELECT column_name
        FROM information_schema.columns 
        WHERE table_name = 'upload_supplier_master_data' AND column_name = 'final_status'
    """))
    
    if not result.fetchone():  # Column does not exist
        op.add_column(
            "supplier_master_data",
            sa.Column(
                "validation_status",
                sa.Enum("MATCH", "NO_MATCH", "PENDING", name="validationstatus"),
                server_default=sa.text("'PENDING'"),
                nullable=False,
            ),
        )
        op.add_column(
            "supplier_master_data",
            sa.Column(
                "final_status",
                sa.Enum("ACCEPTED", "REJECTED", "PENDING", name="finalstatus"),
                server_default=sa.text("'PENDING'"),
                nullable=False,
            ),
        )
        # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("supplier_master_data", "final_status")
    op.drop_column("supplier_master_data", "validation_status")
    op.create_table(
        "orgdata",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "orgname", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.Column(
            "orgidentifier", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.Column("bvdids", sa.VARCHAR(length=100), autoincrement=False, nullable=True),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="orgdata_pkey"),
        sa.UniqueConstraint("bvdids", name="orgdata_bvdids_key"),
        sa.UniqueConstraint("orgidentifier", name="orgdata_orgidentifier_key"),
    )
    op.create_table(
        "matchbvdid",
        sa.Column("bvdid", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("name", sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column(
            "name_international",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("address", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column(
            "postcode", sa.VARCHAR(length=50), autoincrement=False, nullable=True
        ),
        sa.Column("city", sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column(
            "country", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.Column(
            "phone_or_fax", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.Column(
            "email_or_website",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "national_id", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.Column("state", sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column(
            "address_type", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.Column(
            "ens_id", sa.VARCHAR(length=255), autoincrement=False, nullable=False
        ),
        sa.PrimaryKeyConstraint("ens_id", name="matchbvdid_pkey"),
    )
    # ### end Alembic commands ###
