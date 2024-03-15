"""product

Revision ID: fb1391204958
Revises: 0a5674af834f
Create Date: 2024-03-16 13:17:46.572535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb1391204958'
down_revision: Union[str, None] = '0a5674af834f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_suppliers_id'), 'suppliers', ['id'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.drop_index('ix_books_id', table_name='books')
    op.drop_table('books')
    op.drop_index('ix_authors_id', table_name='authors')
    op.drop_table('authors')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('authors_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='authors_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_authors_id', 'authors', ['id'], unique=False)
    op.create_table('books',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], name='books_author_id_fkey'),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='books_category_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='books_pkey')
    )
    op.create_index('ix_books_id', 'books', ['id'], unique=False)
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_suppliers_id'), table_name='suppliers')
    op.drop_table('suppliers')
    # ### end Alembic commands ###
